lis = [int(i) for i in input().split()]
n = lis[0]
k = lis[1]
l = lis[2]
c = lis[3]
d = lis[4]
p = lis[5]
nl = lis[6]
np = lis[7]
slices = c*d
litres = k*l
count = 0
l_curr = litres
s_curr = slices
p_curr = p

while l_curr >= nl and s_curr >= 1 and p_curr >= np :
    l_curr -= nl
    s_curr -= 1
    p_curr -= np
    count += 1
print(count//n)
