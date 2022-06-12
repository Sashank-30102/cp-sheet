n = int(input())
even = []
odd = []
en = 2
on = 1
for i in range(n//2):
    even.append(en)
    en = en + 2
for i in range(n - n//2):
    odd.append(on)
    on = on + 2
if sum(even) > sum(odd):
    while sum(even) > sum(odd) :
        odd[-1] += 2
if sum(even) < sum(odd):
    while sum(even) < sum(odd) :
        even[-1] += 2
if sum(even) == sum(odd) and len(even) != 0:
    print("YES")
    print(*even,*odd)
else :
    print("NO")
    
    
