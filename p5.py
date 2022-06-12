lis = [int(i) for i in input().split()]
a = lis[0]
b = lis[1]
c = lis[2]
mean = (a+b+c)//3
print(abs(mean-a)+abs(mean-b)+abs(mean-c))

