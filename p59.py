l = [int(i) for i in input().split()]
x = l[0]
y = l[1]
z = l[2]
xrem = x-(z*(x//z))
yrem = y-(z*(y//z))
maxrem = max(xrem,yrem)
minrem = min(xrem,yrem)
p = z-maxrem
if p > minrem :
    print(x//z + y//z,0)
else :
    print(x//z + y//z + 1,p)
    
