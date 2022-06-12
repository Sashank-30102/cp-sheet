from itertools import permutations
n = int(input())
lis = [int(i) for i in input().split()]
def check(lis) :
    for i in range(1,len(lis)-1):
        if lis[i-1]+lis[i+1] <= lis[i]:
            return False
    if lis[-1]+lis[1] > lis[0] and lis[-2]+lis[0] > lis[-1]:
        return True
    else :
        return False
perms = list(permutations(lis))
flag = 0
for i in perms:
    if check(i):
        print("YES")
        print(*i)
        flag = 1
        break
if flag == 0:
    print("NO")
