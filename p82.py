from itertools import combinations
import math
lis = [i for i in range(1,int(input())+1)]
subsets = []
for i in range(1,len(lis)+1):
    subsets += list(combinations(lis,i))
flag = 0
for i in range(len(subsets)):
    for j in range(i+1,len(subsets)):
        if math.gcd(sum(subsets[i]),sum(subsets[j])) > 1:
            print("Yes")
            print(len(subsets[i]),*subsets[i])
            print(len(subsets[j]),*subsets[j])
            flag = 1
            break
    if flag == 1:
        break
if flag == 0:
    print("No")

