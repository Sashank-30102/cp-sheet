t = int(input())
for i in range(t):
    n = int(input())
    lis = [i+1 for i in range(n)]
    while len(lis) > 1:
        a = lis[-1]
        b = lis[0]
        lis = lis[::-1]
        for j in lis[1:]:
            if (j+a)%2 == 0:
                b = j
                break
        print(str(a)+" "+str(b))
        lis.remove(a)
        lis.remove(b)
        lis.append((a+b)//2)
        lis.sort()
    print(lis[0])
    
    
    
    
    
