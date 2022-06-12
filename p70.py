l = [int(i) for i in input().split()]
x = l[0]
y = l[1]
s = l[2]
if (s-(x+y))%2 == 0 and s > x+y:
    print("YES")
else :
    print("NO")
