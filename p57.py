l = [int(i) for i in input().split()]
m = l[0]
n = l[1]
count = 0
if m%2 == 0:
    count += (m//2)*n
else :
    count += (m//2)*n + (n//2)
print(count)
