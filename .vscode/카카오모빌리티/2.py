

from collections import deque


def solution(N, A, B):
    graph = [[] for _ in range(N+1)]
    for i,a in enumerate(A):
        graph[a].append(B[i])
    answer = False
    stack = deque()
    stack.append((2,1))
    while stack:
        round,x = stack.pop()
        if round == N:
            answer = True
            break
        for g in graph[x]:
            if g == x+1:
                stack.append((round+1,g))
                break
        else:
            break
    return answer
      
    
    

print(solution(4,[1,2,4,4,3],[2,3,1,3,1]))