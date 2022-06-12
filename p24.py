c = input()
l = input().split()
flag = 0
for i in l:
    if i[0] == c[0] or i[1] == c[1]:
        print("YES")
        flag = 1
        break
if flag == 0:
    print("NO")
