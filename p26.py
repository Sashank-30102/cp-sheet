t = int(input())
lis = []
for i in range(t):
    lis.append(int(input()))
count = 0
n = 1
s = "1"
for i in lis :
    if i == 1:
        print(1)
    else :
        while int(s) != i:
            count += len(s)
            s = s+str(n)
            if int(s) == i:
                count += len(s)
                break
            if len(s) > 4:
                n += 1
                s = str(n)
        print(count)
        count = 0
        n = 1
        s = "1"

