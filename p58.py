l = [int(i) for i in input().split()]
n = l[0]
m = l[1]
k = l[2]
l = [int(i) for i in input().split()]
happiness = 0
max1 = max(l)
l.remove(max1)
max2 = max(l)
flag = 0
while m > k:
    if flag == 0 :
        happiness += max1*k
        m -= k
        flag = 1
    else :
        happiness += max2
        m -= 1
        flag = 0
if flag == 0:
    happiness += max1*m
else :
    happiness += max2 + max1*(m-1)
    
print(happiness)
