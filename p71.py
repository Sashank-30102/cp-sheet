l = [int(i) for i in input().split()]
oddcount = 0
while True:
    for i in l:
        if i%2 != 0:
            oddcount += 1
    if oddcount <= 1:
        print("Yes")
        break
    elif l[0] > 0 and l[1] > 0 and l[2] > 0:
        l[0] -= 1
        l[1] -= 1
        l[2] -= 1
        l[3] += 3
    else :
        print("No")
        break
    oddcount = 0
