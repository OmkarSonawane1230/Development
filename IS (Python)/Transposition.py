def encrypt(s, key):
    return "".join(s[i::key] for i in range(key))

def decrypt(s, key):
    res = [""] * len(s)
    k = 0
    for i in range(key):
        for j in range(i, len(s), key):
            res[j] = s[k]
            k += 1
    return "".join(res)

msg = "HELLOWORLD"
enc = encrypt(msg, 3)
print(enc)
print(decrypt(enc, 3))
