s = input()
lis = [0,0,0]
for i in s:
    if i == "B":
        lis[0] += 1
    elif i == "S":
        lis[1] += 1
    else :
        lis[2] += 1
count = [int(i) for i in input().split()]
prices = [int(i) for i in input().split()]
r = int(input())
c = 0
while r > max(prices) or (count[0] >= lis[0] and count[1] >= lis[1] and count[2] >= lis[2]):
    count[0] = count[0]-lis[0]
    count[1] = count[1]-lis[1]
    count[2] = count[2]-lis[2]
    c += 1
    if count[0] < lis[0] and r >= prices[0]:
        r = r - (lis[0]-count[0])*prices[0]
        count[0] = lis[0]
    elif count[0] < lis[0] and r < prices[0]:
        break
    if count[1] < lis[1] and r >= prices[1]:
        r = r - (lis[1]-count[1])*prices[1]
        count[1] = lis[1]
    elif count[1] < lis[1] and r < prices[1]:
        break
    if count[2] < lis[2] and r >= prices[2]:
        r = r - (lis[2]-count[2])*prices[2]
        count[2] = lis[2]
    elif count[2] < lis[2] and r < prices[2]:
        break
print(c)
        

