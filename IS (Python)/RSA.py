import rsa

msg = b"Hello"
pub, priv = rsa.newkeys(512)

enc = rsa.encrypt(msg, pub)
dec = rsa.decrypt(enc, priv)

print(dec.decode())
