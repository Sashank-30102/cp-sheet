n = int(input())
x = 0
plus_flag = 0
minus_flag = 0
for i in range(n):
    s = input()
    if s == "X++" or "++X":
        x += 1
    elif s == "X--" or "--X":
        x -= 1
print(x)
