n = int(input())
l = [int(i) for i in input().split()]
odd = []
even = []
for i in range(len(l)):
    if i%2 == 0 and l[i]%2 != 0:
        even.append(l[i])
    if i%2 != 0 and l[i]%2 == 0:
        odd.append(l[i])
if len(odd) == len(even):
    print(len(odd))
else :
    print(-1)
