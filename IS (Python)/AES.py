from Crypto.Cipher import AES

msg = b"Hello".ljust(16, b" ")
key = b"1234567890123456"

c = AES.new(key, AES.MODE_ECB)
enc = c.encrypt(msg)
dec = c.decrypt(enc)

print(enc.hex())
print(dec.decode().strip())
