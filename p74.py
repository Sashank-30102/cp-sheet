l = [int(i) for i in input().split()]
n = l[0]
k = l[1]
lis = []
for i in range(n):
    lis.append(1)
i = 0
while sum(lis)%k != 0:
    lis[i] += 1
    i += 1
    if i == len(lis):
        i = 0
print(max(lis))
