n = int(input())
s = input()
sublis = []
for i in range(n):
    for j in range(i+1,n):
        sublis.append(s[i:j])
flag = 0
for i in sublis:
    flag = 0
    ss = set(list(i))
    for j in ss:
        if list(i).count(j) > len(i)//2:
            flag = 1
            break
    if flag == 0:
        print("YES")
        print(i)
        break
if flag == 1:
    print("NO")
