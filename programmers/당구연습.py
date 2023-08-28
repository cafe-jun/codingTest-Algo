

import math


def solution(m: int, n: int, startX: int, startY: int, balls: list[int]):
    answer = []
    # 상 하 좌 우 의 각 거리의 최솟값을 구한후 answer 에 추가 
    for endX,endY in balls: 
        up,down,left,right = float('inf'),float('inf'),float('inf'),float('inf')
        if not (startX==endX and startY > endY):
            down = getDistance(startX,-startY,endX,endY)
        # if not ()
    return answer


def getDistance(x1,y1,x2,y2): 
    return math.sqrt(math.pow(x1-x2,2) + math.pow(y1-y2,2))

print(solution(10,10,3,7,[[7, 7], [2, 7], [7, 3]]))