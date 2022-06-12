t =int(input())
for i in range(t):
    n = int(input())
    l = [int(i) for i in input().split()]
    l.sort()
    print(l[len(l)//2] - l[len(l)//2 - 1])
    
    

