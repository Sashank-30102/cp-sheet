l = [int(i) for i in input().split()]
n = l[0]
m = l[1]
grids = m*n
if grids%2 != 0:
    print(grids//2 + 1)
else:
    print(grids//2)
