n = int(input())
if n <= 14 :
    print("NO")
else :
    n = n%14
    if n in range(1,7):
        print("YES")
    else :
        print("NO")
