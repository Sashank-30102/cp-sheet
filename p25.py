n = int(input())
i = 1
s = 0
a = 0
if n == 1 :
    print(1)
else :
    while(a < n):
        s = s + i
        a = a + s
        if (a >= n):
            break
        i = i + 1
    print(i-1)

