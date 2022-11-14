from itertools import combinations
from timeit import repeat

# 1. 좌표 찾기 
# 2. 좌표 그리기 


def solution(line):
    answer = []
    a = [2,-1,4]
    b = [-2,-1,4]
    result = set()
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    # 1. 좌표 찾기 
    for m in combinations(line,2):
        a,b = m
        de = ((a[0]*b[1])-(a[1]*b[0]))
        if de == 0 :
            continue
        x = ((a[1]*b[2])-(a[2]*b[1]))/de
        y = ((a[2]*b[0])-(a[0]*b[2]))/de
        if float(x).is_integer() == True and float(y).is_integer() == True:
            x = int(x)
            y = int(y)
            result.add((x,y)) 
    for i,k in enumerate(list(result)):
        if i == 0:
            min_x = k[0]
            min_y = k[1]
            max_x = k[0]
            max_y = k[1]
        else:
            min_x = min(k[0],min_x)
            min_y = min(k[1],min_y)
            max_x = max(k[0],max_x)
            max_y = max(k[1],max_y)
    # 2. 좌표 그리기 
    for i in range(max_y-min_y+1):
        answer.append(list('.'*(max_x-min_x+1)))
    for t in list(result):
        answer[t[1]-min_y][t[0]-min_x] = '*'
    answer2 = []
    for ans in reversed(answer):
        answer2.append(''.join(ans))
    return answer2


print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]) ==	["....*....", ".........", ".........", "*.......*", ".........", ".........", ".........", ".........", "*.......*"])
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]) == ["*.*"])
print(solution([[1, -1, 0], [2, -1, 0]]) ==	["*"])
print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]])==["*"])

