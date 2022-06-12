t = int(input())
for i in range(t):
    l = [int(i) for i in input().split()]
    m = l[0]
    n = l[1]
    matrix = []
    for i in range(m):
        matrix.append(input())
    count = 0
    for i in range(m):
        if matrix[i][n-1] == "R":
            matrix[i][n-1] == "D"
            count += 1
    for i in range(n):
        if matrix[m-1][i] == "D":
            matrix[m-1][i] == "R"
            count += 1
    print(count)
