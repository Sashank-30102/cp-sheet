l = [int(i) for i in input().split()]
n = l[0]
k = l[1]
l = [int(i) for i in input().split()]
l.sort()
s = 0
count = 0
lis = []
for i in l:
    if s + i <= k:
        count = count + 1
        s = s+i
        lis.append(i)
    else :
        break
print(count)
print(*lis)

