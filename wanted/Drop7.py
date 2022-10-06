
matrix = []
# for _ in range(7):
#     matrix.append(list(map(int, input().split())))
#ball = int(input())

f = open('test.txt')
for _ in range(7):
    matrix.append(list(map(int, f.readline().split())))
ball = int(f.readline())
f.close()

# 연속해서 놓인 값에 대해서 놓아보자
# 세로 그룹 가로 그룹 체크
# 가장 높은수의 가로 세로 그룹에 두는것이 좋다
# 제일 아래다가 두는것이 좋음
# 제일 큰숫자를 찾아 dfs의 좌표로 넣자
max_t = []
max_v = 0
for i in range(7):
    for j in range(7):
        if max_v < matrix[i][j]:
            max_t.clear()
            max_t.append((i, j))
            max_v = matrix[i][j]
        elif max_v == matrix[i][j]:
            max_t.append((i, j))


def dfs(x, y):
    s = len(matrix[x][y])


print(max_t)

print(ball)
