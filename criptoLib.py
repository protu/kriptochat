"""Module with basic cripto funcions"""
import bcrypt
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES
from Crypto import Random

sym_key_len = 24
chunk_size = 214
block_size = AES.block_size


def get_iv():
    return Random.new().read(block_size)


def create_keys(directory=".", key_length=2048):
    """Create private/public key pair and  and store it in file"""
    try:
        # Create file with private key
        sec_key = RSA.generate(key_length)
        sec_key_file = open(directory + "/seckey.pem", "wb")
        sec_key_file.write(sec_key.exportKey())
        sec_key_file.close()
        # Create file with public key
        pub_key_file = open(directory + "/pubkey.pem", "wb")
        pub_key = sec_key.publickey()
        pub_key_file.write(pub_key.exportKey())
        pub_key_file.close()
    except Exception as e:
        print(e)
    return True


def encrypt_key(key, directory=".", pk=None):
    """Encrypt secret key with public key"""
    if pk is None:
        pub_key_file = open(directory + "/pubkey.pem", "rb")
        public_key = RSA.importKey(pub_key_file.read())
    else:
        public_key = RSA.importKey(pk)
    pub_key = PKCS1_OAEP.new(public_key)
    key += bytes(" " * (chunk_size - len(key)), "utf-8")
    return pub_key.encrypt(key)


def decrypt_key(enc_key, directory=".", sk=None):
    """Decrypt secret key with private key"""
    if sk is None:
        sec_key_file = open(directory + "/seckey.pem", "rb")
        secret_key = RSA.importKey(sec_key_file.read())
    else:
        secret_key = RSA.importKey(sk)
    sec_key = PKCS1_OAEP.new(secret_key)
    sym_key = sec_key.decrypt(enc_key).strip()
    return sym_key


def hash_pass(password):
    """Make hash from password"""
    return bcrypt.hashpw(bytes(password, "utf-8"), bcrypt.gensalt())


def check_pass(password, hashed_pass):
    """Check if password is right"""
    return bcrypt.checkpw(bytes(password, "utf-8"), bytes(hashed_pass, "utf-8"))


def create_sym_key():
    return Random.new().read(sym_key_len)


def enc_msg(msg, key, iv):
    """Encrypt plain text message with secret key"""
    msg_len = len(msg)
    msg = bytes(str(msg_len) + "#" + msg, "utf-8")
    chipper = AES.new(key, AES.MODE_CBC, iv)
    chunk = bytes()
    offset = 0
    end = False
    while not end:
        msg_chunk = msg[offset: offset + block_size]
        if len(msg_chunk) % block_size != 0:
            msg_chunk += bytes("%" * (block_size - len(msg_chunk)), "utf-8")
            end = True
        chunk += chipper.encrypt(msg_chunk)
        offset += block_size
    return iv + chunk


def dec_msg(msg, key):
    """Decrypt chipper to plan text"""
    iv = msg[:block_size]
    msg = msg[block_size:]
    chipper = AES.new(key, AES.MODE_CBC, iv)
    message = str(chipper.decrypt(msg), "utf-8")
    msg_start = message.find("#")
    msg_len = int(message[:msg_start])
    return message[msg_start + 1:(msg_len + msg_start + 1)]
