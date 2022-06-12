l = [int(i) for i in input().split()]
k = l[0]
r = l[1]
i = 1
n = k
while (True):
    if n%10 == r or n%10 == 0:
        print(i)
        break
    else :
        i += 1
        n = k*i
