s = "Hello\nWorld"

print("".join(chr(ord(c) ^ 127) for c in s))
print("".join(chr(ord(c) & 127) for c in s))
