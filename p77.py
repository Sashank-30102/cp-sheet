l = [int(i) for i in input().split()]
a = l[0]
b = l[1]
c = l[2]
flag = 0
shotcount = 0
for i in range(1000):
    if l[i%3] > 1:
        l[i%3] -= 1
        shotcount += 1
    
    if shotcount%6 == 0 and shotcount != 0:
        l[0] -= 1
        l[1] -= 1
        l[2] -= 1
        if l[0] == 0 and l[1] == 0 and l[2] == 0:
            print("YES")
            flag = 1
            break
        shotcount += 1
    
    if l[0] <= 1 and l[1] <= 1 and l[2] <= 1 and shotcount%6 != 0:
        break
    
if flag == 0:
    print("NO")
    
    
