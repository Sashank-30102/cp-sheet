l = [int(i) for i in input().split()]
a = l[0]
b = l[1]
m = min(a,b)
if 2*m > max(a,b):
    print(m*m*4)
else :
    print(max(a,b)**2)
