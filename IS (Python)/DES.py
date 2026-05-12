from Crypto.Cipher import DES

msg = b"Hello".ljust(8, b" ")
key = b"12345678"

c = DES.new(key, DES.MODE_ECB)
enc = c.encrypt(msg)
dec = c.decrypt(enc)

print(enc.hex())
print(dec.decode().strip())
