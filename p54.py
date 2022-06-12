n = int(input())
if n < 3:
    print(0)
else:
    if n%2 == 1:
        print(n//2)
    else :
        print(n//2 - 1)
