n = int(input())
lis = []
for i in range(n):
    lis.append(int(input()))

for i in range(len(lis)):
    if lis[i] > 0:
        lis[i] = lis[i]//2
    elif lis[i] < 0:
        lis[i] = lis[i]//2 + 1
            
if sum(lis) > 0:
    for i in range(len(lis)):
        if lis[i] < 0:
            lis[i] -= 1
        if sum(lis) == 0:
            break
if sum(lis) < 0:
    for i in range(len(lis)):
        if lis[i] > 0:
            lis[i] += 1
        if sum(lis) == 0:
            break

for i in lis:
    print(i)
