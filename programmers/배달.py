from collections import deque


def solution(N: int, road: list[int], K: int):
    answer = 1
    road.sort( key= lambda x: x[0])
    INF= 1e9
    # 1에서 N 까지 가는데 최소 거리를 리스트로 
    matrix = [[INF for _ in range(N+1)] for _ in range(N+1)];
    # 이차원 배열에 그리기  
    for r in road:
        matrix[r[0]][r[1]] = min(r[2],matrix[r[0]][r[1]])
        matrix[r[1]][r[0]] = min(r[2],matrix[r[1]][r[0]])
    
    # 탐색 
    for l in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                if i != j and i != l and l != j:
                    matrix[i][j] = min(matrix[i][l] + matrix[l][j],matrix[i][j])
    for m in matrix[1]:
        #print(m)
        if m <= K:
            answer+= 1

    return answer


print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))
print(solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4))