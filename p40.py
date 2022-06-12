l = [int(i) for i in input().split()]
a = l[0]
b = l[1]
c = l[2]
d = l[3]
flag = 0
def checkTriangle(a,b,c):
    if a+b > c and b+c > a and a+c > b:
        return (True)
    else:
        return (False)
for i in range(a,b+1):
    for j in range(b,c+1):
        for k in range(c,d+1):
            if checkTriangle(i,j,k):
                print(i,j,k)
                flag = 1
                break
        if flag == 1:
            break
    if flag == 1:
        break
    
            

