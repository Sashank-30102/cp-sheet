t = int(input())
lis = []
for i in range(t):
    lis.append(input())
for i in lis :
    flag = 0
    count = 0
    l = []
    for j in i:
        if j == "1":
            flag += 1
            l.append(count)
            count = 0
        if flag > 0 and j == "0":
            count += 1
    if i[-1] == "0" and len(l) > 0:
        l.pop()
    s = 0
    for i in l:
        s = s + int(i)
    print(s)
            
