def hcf(a,b):
    if(b == 0):
        return a
    else:
        return hcf(b, a % b)
        
l = [int(i) for i in input().split()]
a = l[0]
b = l[1]
c = l[2]
flag = 0
for i in range(10**(a-1),10**a):
    for j in range(10**(b-1),10**b):
        if len(str(hcf(i,j))) == c:
            flag = 1
            print(i,j)
            break
    if flag == 1:
        break
