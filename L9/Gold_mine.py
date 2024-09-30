rock = [[7, 0, 0, 0, 0, 0, 0],
        [5, 8, 0, 0, 0, 0, 0],
        [9, 8, 2, 0, 0, 0, 0],
        [1, 3, 5, 6, 0, 0, 0],
        [6, 2, 4, 4, 5, 0, 0],
        [9, 5, 3, 5, 5, 7, 0],
        [7, 4, 6, 4, 7, 6, 8]]


def max_gold(mat, m, n):
    gold_table = [[0 for i in range(n)]
                  for j in range(m)]
    right_down = 0
    down = 0
    for col in range(n - 1, -1, -1):
        for row in range(m):
            if row == m - 1 or col == n - 1:
                right_down = gold_table[row - 1][col - 1]
            if row == m - 1 or col == n:
                down = gold_table[row - 1][col]
            gold_table[row][col] = mat[row][col] + max(right_down, down)
    print(gold_table)
    result = gold_table[0][0]
    for i in range(0, m):
        result = max(result, gold_table[i][0])
    return result


print(max_gold(rock, 7, 7))
