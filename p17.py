l = [int(i) for i in input().split()]
k = l[0]
n = l[1]
w = l[2]
amount = 0
for i in range(1,w+1):
    amount += i*k
if amount > n:
    print(amount-n)
else :
    print(0)

