import criptoLib

msg = '''The house stood on a slight rise just on the edge of the village. It stood on
its own and looked over a broad spread of West Country farmland. Not a
remarkable house by any means—it was about thirty years old, squattish,
squarish, made of brick, and had four windows set in the front of a size and
proportion which more or less exactly failed to please the eye.
The only person for whom the house was in any way special was Arthur Dent, and
that was only because it happened to be the one he lived in. He had lived in it
for about three years, ever since he had moved out of London because it made him
nervous and irritable. He was about thirty as well, dark haired and never quite
at ease with himself. The thing that used to worry him most was the fact that
people always used to ask him what he was looking so worried about. He worked in
local radio which he always used to tell his friends was a lot more interesting
than they probably thought. It was, too—most of his friends worked in
advertising.
It hadn’t properly registered with Arthur that the council wanted to knock down
his house and build an bypass instead.
At eight o’clock on Thursday morning Arthur didn’t feel very good. He woke up
blearily, got up, wandered blearily round his room, opened a window, saw a
bulldozer, found his slippers, and stomped off to the bathroom to wash.'''

# Kreiraj novi par ključeva
key = criptoLib.create_sym_key()
# Kreiraj inicialization vector
iv = criptoLib.get_iv()
# Kriptiraj poruku sa simetričnim ključem koristeći AES192
enc_msg = criptoLib.enc_msg(msg, key, iv)
# Šifriraj ključ putem RSA256 i javnog ključa
ek = criptoLib.encrypt_key(key)
# Dešifriraj ključ za AES
k = criptoLib.decrypt_key(ek)
# Dešifriraj poruku
dec_msg = criptoLib.dec_msg(enc_msg, k)
# Ispiši poruku
print(dec_msg)
