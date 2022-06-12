from itertools import permutations
s = input()
perms = list(permutations(s))
perms = ["".join(i) for i in perms]
flag = 0
for i in perms:
    if int(i)%60 == 0:
        print("red")
        flag = 1
        break
if flag == 0:
    print("cyan")

