def checkprime(n):
    if n%2 == 0 and n != 2:
        return False
    if n == 1:
        return False
    elif n == 2 or n == 3 :
        return True
    else :
        for i in range(2,n//2):
            if n%i == 0:
                return False
        return True
        
n = int(input())
lis = []
for i in range(n):
    lis.append([int(i) for i in input().split()])
print()
for i in lis:
    for j in range(i[0],i[1]+1):
        res = checkprime(j)
        if res :
            print(j)
    print()

