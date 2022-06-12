l = [int(i) for i in input().split()]
n = l[0]
t = l[1]
l = [int(i) for i in input().split()]
curr = 0
while curr+1 < t :
    curr = curr + l[curr]
if curr+1 == t:
    print("YES")
else :
    print("NO")
    
