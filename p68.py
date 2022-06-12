l = [int(i) for i in input().split()]
x = l[0]
y = l[1]
flag = 0
xprev = 0
if x == y:
    print("YES")
else :
    while x != y :
        
        if x%2 == 0 and x < y:
            if int(x*1.5) <= xprev:
                print("NO")
                flag = 1
                break
            x = int(x*1.5)
        elif x > y or x%2 != 0:
            xprev = x
            x = x - 1 
        else :
            print("NO")
            flag = 1
            break
        
    if flag == 0:
        print("YES")
            
        
        
