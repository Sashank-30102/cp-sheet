l = [int(i) for i in input().split()]
n = l[0]
m = l[1]
a = l[2]
x = n//a
y = m//a
if n%a != 0:
    x += 1
if m%a != 0:
    y += 1
print(x*y)
