l = [int(i) for i in input().split()]
coordinates = [(0,0),(0,l[1]),(l[0],0),(l[0],l[1])]
h = l[1]
w = l[0]
l = [int(i) for i in input().split()]
x0 = []
xh = []
y0 = []
yw = []
for i in l[1:]:
    x0.append((i,0))
l = [int(i) for i in input().split()]
for i in l[1:]:
    xh.append((i,h))
l = [int(i) for i in input().split()]
for i in l[1:]:
    y0.append((0,i))
l = [int(i) for i in input().split()]
for i in l[1:]:
    yw.append((w,i))
x0.sort(key = lambda x: x[1])
xh.sort(key = lambda x: x[1])
y0.sort(key = lambda x: x[0])
yw.sort(key = lambda x: x[0])

def eucdist(p1,p2):
    d = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
    d = d**0.5
    return d

basex0 = eucdist(x0[0],x0[-1])
basexh = eucdist(xh[0],xh[-1])
basey0 = eucdist(y0[0],y0[-1])
baseyw = eucdist(yw[0],yw[-1])
base = max(basex0,basexh,basey0,baseyw)

print(int(base*min(h,w)))
            
        
