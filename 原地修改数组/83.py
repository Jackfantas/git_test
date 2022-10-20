A = [[0, 6, 0], [2, 0, 0], [0, 1, 0]]

step = 0

def move_stone(i, j, step):
    # up
    if i - 1 >= 0 and sorted_A[i - 1][j] == 0 and sorted_A[i][j] > 1:
        step += 1
        sorted_A[i][j] -= 1
    # down
    if i + 1 < 3 and sorted_A[i + 1][j] == 0 and sorted_A[i][j] > 1:
        step += 1
        sorted_A[i][j] -= 1
    # left
    if j - 1 >= 0 and sorted_A[i][j - 1] == 0 and sorted_A[i][j] > 1:
        step += 1
        sorted_A[i][j] -= 1
    # right
    if j + 1 < 3 and sorted_A[i][j + 1] == 0 and sorted_A[i][j] > 1:
        step += 1
        sorted_A[i][j] -= 1
    return step

# sort the A by the sum of each row, decending
sorted_A = sorted(A, key=lambda x: sum(x), reverse=True)
print(sorted_A)
for row in range(3):
    for col in range(3):
        if sorted_A[row][col] > 1:
            step = move_stone(row, col, step)
            print(step)
            if sorted_A[row][col] > 1:
                sorted_A[row + 1][col] += sorted_A[row][col] - 1
                step += (sorted_A[row][col] - 1)

                print((sorted_A[row][col] - 1))
print(step)
