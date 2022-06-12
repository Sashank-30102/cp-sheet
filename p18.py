lis = [int(i) for i in input().split()]
l = lis[0]
b = lis[1]
count = 0
while l <= b :
    l = l*3
    b = b*2
    count += 1
print(count)
