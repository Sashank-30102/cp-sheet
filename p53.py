l = [int(i) for i in input().split()]
a = l[0]
b = l[1]
count = 0
while a != b:
    if a > b:
        if a-b > 9:
            b = b+ 10
        else :
            b = a
    else :
        if b-a > 9:
            a = a+10
        else :
            a = b
    count+=1 
if a == b:
    print(count)
