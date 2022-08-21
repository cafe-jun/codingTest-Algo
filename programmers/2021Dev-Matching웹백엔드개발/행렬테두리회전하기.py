from copy import deepcopy


def solution(rows, columns, queries):
    answer = []
    cnt = 0
    board = []
    for c in range(rows):
        board.append([])
        for r in range(columns):
            cnt += 1
            board[-1].append(cnt)

    for query in queries:
        x1, y1, x2, y2 = query

        tmp_board = deepcopy(board)
        tmp_answer = set()
        min_num = 1e9
        x_point = x1-1
        y_point = y1-1
        for i in range(y2-y1):
            board[x_point][y_point+1],board[x_point][y_point] = board[x_point][y_point],board[x_point][y_point+1]
            tmp_answer.add(tmp_board[x_point][y_point])
            y_point -= 1
        for i in range(x2-x1):
            tmp_board[x_point][y_point],board[x_point+1][y_point] = tmp_board[x_point][y_point],board[x_point+1][y_point]
            tmp_answer.add(tmp_board[x_point][y_point])
            x_point -= 1
        for j in range(y2-y1):
            tmp_board[x_point][y_point],board[x_point][y_point-1] = board[x_point][y_point-1],tmp_board[x_point][y_point]
            tmp_answer.add(tmp_board[x_point][y_point])
            y_point += 1
        for j in range(x2-x1):
            tmp_board[x_point][y_point],board[x_point-1][y_point] = board[x_point-1][y_point],tmp_board[x_point][y_point]
            tmp_answer.add(tmp_board[x_point][y_point])
            x_point += 1
        min_num = min(tmp_answer)
        answer.append(min_num)
    return answer


# moveX = [0, 1, 0, -1]
# moveY = [1, 0, -1, 0]
# def make_matrix(rows, columns):
#     matrix = [[0] * columns for _ in range(rows)]
#     for i in range(1, rows + 1):
#         for j in range(1, columns + 1):
#             matrix[i - 1][j - 1] = (columns * (i - 1)) + j

#     return matrix

# def rotate(queries, matrix):
#     ar, ac, br, bc = queries
#     mins = []
#     ar -= 1
#     ac -= 1
#     br -= 1
#     bc -= 1
#     for i in range(bc-1, ac-1, -1):
#         matrix[ar][i], matrix[ar][i + 1] = matrix[ar][i + 1], matrix[ar][i]
#         mins.append(matrix[ar][i])
#         mins.append(matrix[ar][i + 1])
#     for i in range(ar, br):
#         matrix[i][ac], matrix[i + 1][ac] = matrix[i + 1][ac], matrix[i][ac]
#         mins.append(matrix[i][ac])
#         mins.append(matrix[i + 1][ac])
#     for i in range(ac, bc):
#         matrix[br][i], matrix[br][i+1] = matrix[br][i+1], matrix[br][i]
#         mins.append(matrix[br][i])
#         mins.append(matrix[br][i+1])
#     for i in range(br-1, ar, -1):
#         matrix[i][bc], matrix[i+1][bc] = matrix[i+1][bc], matrix[i][bc]
#         mins.append(matrix[i][bc])
#         mins.append(matrix[i+1][bc])
#     mins = set(mins)
#     return (matrix, min(mins))


def solution(rows, columns, queries):
    matrix = make_matrix(rows, columns)
    result = []
    for q in queries:
        matrix, MIN = rotate(q, matrix)
        result.append(MIN)
    return result



print(
    solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]) == [8, 10, 25])
print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [
      2, 1, 3, 2], [2, 2, 3, 3]]) == [1, 1, 5, 3])
print(solution(100, 97, [[1, 1, 100, 97]]) == [1])






