num = int(input())
for i in range(num):
    l = [int(i) for i in input().split()]
    count = 0
    a = l[0]
    b = l[1]
    n = l[2]
    while a <= n and b <= n:
        if min(a,b) == a:
            a = a + b
        else :
            b = a + b
        count += 1
    print(count)
    
