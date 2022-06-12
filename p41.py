def compute_lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm
flag = 0
lis = [int(i) for i in input().split()]
l = lis[0]
r = lis[1]
for i in range(l,r+1):
    for j in range(i+1,r+1):
        if compute_lcm(i,j) in range(l,r+1):
            print(i,j)
            flag =1
            break
    if flag == 1:
        break
if flag == 0:
    print(-1,-1)
    

