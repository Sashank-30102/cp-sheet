l = [int(i) for i in input().split()]
a = l[0]
b = l[1]
c = l[2]
n = l[3]
m = max(a,b,c)
if m-a < n:
    n = n - (m-a)
    a = m
if m-b < n:
    n = n - (m-b)
    b = m
if m-c < n:
    n = n - (m-c)
    c = m
while n > 0:
    a = a + 1
    n = n - 1
    if n > 0:
        b = b + 1
        n = n - 1
    if n > 0:
        c = c + 1
        n = n - 1
if a == b and a == c:
    print("YES")
else :
    print("NO")

