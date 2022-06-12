l = [int(i) for i in input().split()]
x = l[0]
y = l[1]
l = [int(i) for i in input().split()]
a = l[0]
b = l[1]
amount = 0
while x != 0 or y != 0:
    if x > 0 and y > 0:
        x = x - 1
        y = y - 1
        amount += b
    elif x < 0 and y < 0:
        x = x + 1
        y = y + 1
        amount += b
    elif x > 0 :
        x = x - 1
        amount += a
    elif y > 0 :
        y = y - 1
        amount += a
    elif x < 0 :
        x = x + 1
        amount += a
    elif y < 0 :
        y = y + 1
        amount += a
print(amount)
