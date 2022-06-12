l = [int(i) for i in input().split()]
k = l[0]
x = l[1]
def droot(n):
    n = str(n)
    while(len(n) > 1):
        lis = [int(i) for i in n]
        n = str(sum(lis))
    return int(n)
i = 1
while k > 0:
    if droot(i) == x:
        k = k-1
    if k == 0:
        print(i)
        break
    i += 1
