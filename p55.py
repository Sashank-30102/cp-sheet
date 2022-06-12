l = [int(i) for i in input().split()]
a = l[0]
b = l[1]
count = 0
while a%b != 0:
    a = a+1
    count += 1
if a%b == 0:
    print(count)
