l = [int(i) for i in input().split()]
n = l[0]
x = l[1]
y = l[2]
flag = 0
l = [int(i) for i in input().split()]
for i in range(n):
    flag = 0
    if i-x < 0 :
        p = 0
    else :
        p = i-x
    if i+y >= n :
        q = n
    else :
        q = i+y+1

    for j in l[p:i]:
        if j < l[i]:
            flag = 1
            break
    if flag == 0:
        for j in l[i+1:q] :
            if j < l[i]:
                flag = 1
                break
    if flag == 0:
        print(i+1)
        break
        
        
