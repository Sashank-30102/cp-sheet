n = int(input())
lis = [int(i) for i in input().split()]
prev = lis[-1]
s = lis[-1]
lisrev = lis[::-1]
for i in lisrev[1:]:
    if i < prev:
        s += i
        prev = i
    else :
        s += prev-1
        prev = prev-1
    if prev == 0:
        break
print(s)
