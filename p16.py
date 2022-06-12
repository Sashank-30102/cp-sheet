num = int(input())
n = int(input())
for i in range(n):
    if num%10 == 0:
        num = num / 10
    else :
        num = num - 1
print(int(num))
