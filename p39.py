n = int(input())
for i in range(n+1):
    if (i != n):
        print(" "*(2*n - 2*i - 1),end = " ")
    for j in range(i+1):
        print(j,end = " ")
    for k in range(i,0,-1):
        print(k-1,end = " ")
    print()
for i in range(n):
    print(" "*2*(i+1),end = "")
    for j in range(n-i):
        print(j,end = " ")
    for k in range(n-i-2,-1,-1):
        print(k,end = " ")
    print()
