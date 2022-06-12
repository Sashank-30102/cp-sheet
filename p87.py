l = [int(i) for i in input().split()]
n = l[0]
m = l[1]
lis = []
flag = 0
num = n
while num > 0:
    if num > 1:
        lis.append(2)
        num = num - 2
    elif num == 1:
        lis.append(1)
        num = num - 1
def checklis(lis):
    for i in lis:
        if i != 1:
            return True
    return False
while checklis(lis):
    if len(lis)%m == 0:
        print(len(lis))
        flag = 1
        break
    else:
        lis.remove(2)
        lis.append(1)
        lis.append(1)
if flag == 0:
    print(-1)
        
