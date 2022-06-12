n = int(input())
l = [int(i) for i in input().split()]
c = 0
s = 0
for i in range(1,len(l)):
    if l[i] > l[i-1] :
        s += 1
        if s > c:
            c = s
    else :
        s = 0
print(c+1)
