n = int(input())
l = [int(i) for i in input().split()]
i = 0
while n > 0:
    n = n - l[i]
    i = i+1
    if n <= 0:
        print(i)
        break
    if n > 0 and i == 7:
        i = 0
    
