n = int(input())
lis = [int(i) for i in input().split()]
maxIndex = lis.index(max(lis))
swapcount = 0
for i in range(maxIndex,0,-1):
    lis[i],lis[i-1] = lis[i-1],lis[i]
    swapcount += 1
lis = lis[::-1]
minIndex = lis.index(min(lis))
for i in range(minIndex,0,-1):
    lis[i],lis[i-1] = lis[i-1],lis[i]
    swapcount += 1
print(swapcount)
    
