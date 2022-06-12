n = int(input())
c = 0
j = 1
for i in range(1,n+1):
    if i == 1 or i == 2:
        c = c + i
    else :
        c = c + i + j
        j += i-1
print(c)
