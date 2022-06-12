matrix = []
for i in range(5):
    matrix.append([int(i) for i in input().split()])
i_index = [0,0]
for i in matrix :
    flag = 0
    for j in i:
        if j == 1:
            i_index[0] = i.index(j)
            i_index[1] = matrix.index(i)
            flag = 1
            break
    if flag == 1:
        break
move_count = 0
move_count += abs(2 - i_index[0]) + abs(2 - i_index[1])
print(move_count)

        
