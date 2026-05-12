import hashlib

msg = "Hello"
enc = hashlib.md5(msg.encode()).hexdigest()
print(enc)
