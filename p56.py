x = int(input())
count = 0
while x > 0:
    if x >= 5:
        x = x - 5
    else :
        x = 0
    count += 1
print(count)
