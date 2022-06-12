lis = [int(i) for i in input().split()]
n = lis[0]
m = lis[1]
flag = 0
for i in range(n):
    if i%2 == 0:
        print("#"*m)
    else :
        if flag == 0:
            print("."*(m-1) + "#")
            flag = 1
        else :
            print("#" + "."*(m-1))
            flag = 0
    
