l = [int(i) for i in input().split()]
n = l[0]
x = l[1]
t = 2
floor = 1
if n <=2 :
    print(floor)
else :
    while n > t:
        t = t+x
        floor += 1
        if n <=t:
            print(floor)
            break
        
