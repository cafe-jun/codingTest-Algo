from collections import deque

def find_tree(a,edges):
    dic = {} 
    for edge in edges:
        start,end = edge
        
        if start not in dic.keys():
            dic[start] = []
        if end not in dic.keys():
            dic[end] = []

        dic[start].append(end)
        dic[end].append(start)
        
    q = deque([(-1,0)])
    path = []
    visited = [0] * len(a)
    visited[0] = 1
        
    while q:
        p,c = q.popleft()
        path.append((p,c))
        des = dic[c]
        if des:
            for d in des:
                if not visited[d]:
                    q.append((c,d))
                    visited[d] = True
                    
    return path[::-1]    

def solution(a, edges):
    answer = 0
    path = find_tree(a,edges)
    
    for parent,child in path[:-1]:
        c_weight = a[child]
        answer += abs(c_weight)
        a[child] += -1 * c_weight
        a[parent] += c_weight
    return answer if a[0] == 0 else -1 


# def solution(a: list[int], edges:list[list[int]]):
#     answer = 0
#     # 절대 값의 가장 큰 기준으로 정렬 
#     # 간선 graph 완성 시키기  
#     # 못 풀겠다 
#     # 위상 정렬에 대해서 알아보자 
#     # 진입 차수 진출 차수 구하기 
#     # 모든 노드에 대한 진입차수를 0으로 초기화 
#     indegree = [0] * (len(a))
#     # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
#     graph = [[] for _ in range(len(a))]
    
#     for e in edges:
#         start,end = e
#         graph[start].append(end)
#         # 진입차수 늘리기 
#         indegree[end] += 1
    
#     print(indegree)
#     def topology_sort():
#         # 알고리즘의 수행결과를 담을 리스트 
#         result = [] 
#         # q 할당 
#         q = deque()
#         # 처음 시작할떄는 진입차수가 0인 노드를 큐에 삽입 
#         for i in range(len(a)):
#             if indegree[i] == 0:
#                 q.append(i)
#         # 큐가 비울때 까지 
#         while q:
#             now = q.popleft()
#             result.append(now)
#             # 해당 원소에서 진입차수 노드들의 1을 빼기 
#             for i in graph[now]:
#                 indegree[i] -= 1 
#                 if indegree[i] == 0:
#                     q.append(i)
                    
#         print(result)
#         return result
#     t_list = topology_sort()
#     result = 0            
#     for t in t_list:
#         print(str(t) + ' ' +str(a))
#         result += a[t]
#         answer += abs(a[t])
    
#     print(result)
#     return answer if result == 0 else -1





# class Node():
#     def __init__(self,line: dict):
#       self.weighted = line["weighted"]
#       self.key = line["key"]
#       self.children = {}

# class NodeTree():
#     result: dict
#     def __init__(self):
#         self.head = Node(None)
#         self.result = {}
    
#     def insert(self,lines: list[dict],):
#         current_node =  self.head
        
#         for line in lines:
#             current_node.children[line["key"]] = Node(line)

        


print(solution([-5,0,2,1,2],[[0,1],[3,4],[2,3],[0,3]])==9)
print(solution([0,1,0],[[0,1],[1,2]])==-1)
