s = input()
if ord(s[0]) >= 97:
    n = ord(s[0])
    s = list(s)
    s[0] = chr(n-32)
    s = "".join(s)
print(s)

