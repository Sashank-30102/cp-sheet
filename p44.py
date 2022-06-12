n = int(input())
l = [int(i) for i in input().split()]
flag = 0
if sum(l)%2 != 0:
    print("YES")
    flag = 1
else :
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if (l[i]%2 == 0 and l[j]%2 == 1) or (l[i]%2 == 1 and l[j]%2 == 0):
                print("YES")
                flag = 1
                break
        if flag == 1:
            break
if flag == 0:
    print("NO")
                
