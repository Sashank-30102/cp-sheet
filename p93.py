n = int(input())
l = ["4"]
s = sum([int(i) for i in l])
while n > s:
    flag = 0
    for i in range(len(l)-1,-1,-1) :
        if l[i] == "4":
            l[i] = "7"
            flag = 1
            break
    if flag == 0:
        for i in range(len(l)):
            l[i] = "4"
        l.append("4")
    s = sum([int(i) for i in l])
if n == s:
    print("".join(l))
else :
    print(-1)
    
           
