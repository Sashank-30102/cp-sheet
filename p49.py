l = [int(i) for i in input().split()]
x = l[0]
y = l[1]
n = l[2]
k = 0
for i in range(n,-1,-1):
    if i%x == y:
        k = i
        break
print(k)
