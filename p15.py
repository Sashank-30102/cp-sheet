n = int(input())
min_cap = 0
currcap = 0
for i in range(n):
    lis = [int(i) for i in input().split()]
    currcap -= lis[0]
    currcap += lis[1]
    if currcap > min_cap :
        min_cap = currcap
print(min_cap)
