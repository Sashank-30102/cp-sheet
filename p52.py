l = [int(i) for i in input().split()]
m = max(l[0],l[1],l[2],l[3])
l.remove(m)
apb = l[0]
bpc = l[1]
apc = l[2]
x = apb-apc
b = (bpc+x)//2
a = apb-b
c = bpc-b
print(a,b,c)
