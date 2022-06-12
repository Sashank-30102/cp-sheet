n = int(input())
lis = []
for i in range(n):
    lis.append([int(i) for i in input().split()])
sumx = 0
sumy = 0
sumz = 0
for i in lis:
    sumx += i[0]
    sumy += i[1]
    sumz += i[2]
    
if sumx == 0 and sumy == 0 and sumz == 0:
    print("YES")
else :
    print("NO")
