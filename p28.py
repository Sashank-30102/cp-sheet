n = int(input())
t = input()
i = 1
s = 0
st = ""
while s < n:
    st = st + t[s]
    s = s+i
    i = i+1
print(st)
