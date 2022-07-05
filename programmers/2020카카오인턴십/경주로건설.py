from collections import deque


def solution(board: list[int]):
    answer = 0
    n = len(board)
    matrix_b = [[400*(n*n) for _ in range(n)] for _ in range(n)]
    matrix_b[0][0] = 100
    q = deque()

    q.append((0, 0, 'v'))
    q.append((0, 0, 'h'))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visted = []
    while q:
        x, y, d = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n:
                temp_b = matrix_b[x][y]
                temp_d = d
                if d == 'h' and i in [0, 1]:
                    temp_b += 400
                    temp_d = 'v'
                elif d == 'v' and i in [2, 3]:
                    temp_b += 400
                    temp_d == 'h'
                else:
                    temp_b += 100
                if (nx, ny, temp_d) not in visted:
                    matrix_b[nx][ny] = min(temp_b, matrix_b[nx][ny])
                    q.append((nx, ny, temp_d))
                    visted.append((nx, ny, temp_d))
    print(matrix_b)
    return answer


print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 900)
print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [
      0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]) == 3800)
print(solution([[0, 0, 1, 0], [0, 0, 0, 0],
      [0, 1, 0, 1], [1, 0, 0, 0]]) == 900)
print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 2100)
print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [
      1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]) == 3200)
