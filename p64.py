n = int(input())
n = n//2
lis = []
for i in range(1,n):
    if {i,n-i} not in lis and i != n-i:
        lis.append({i,n-i})
print(len(lis))
