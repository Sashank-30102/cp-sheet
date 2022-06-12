l = [int(i) for i in input().split()]
n = l[0]
m = l[1]
k = l[2]
cpp = n//k
lis = [0]*(n)
count = 0
if m <= cpp :
    print(m)
else :
    m = m-cpp
    while m > 0:
        lis[count]+=1
        m = m - 1
        count += 1
        if count == k-1:
            count = 0
    print(cpp-max(lis))
        
