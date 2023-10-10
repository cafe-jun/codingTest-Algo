def solution(N, relation, dirname):
    # 디렉토리 관계와 이름 정보 저장
    graph = {i: [] for i in range(1, N+1)}
    names = {i: dirname[i-1] for i in range(1, N+1)}

    # 관계 정보 기반으로 그래프 생성
    for parent, child in relation:
        graph[parent].append(child)

    # DFS 함수 정의
    def dfs(node):
        max_length = 0
        if node not in graph:
            return len(names[node])
        for child_node in graph[node]:
            max_length = max(max_length, dfs(child_node) + len(names[node]) + 1)
        return max_length

    # 최상위 디렉토리부터 DFS 시작 
    return dfs(1) - 1  # root 부터 시작하기 때문에 마지막 '/' 제거

print(solution(7,
               [[1,2],[2,5],[2,6],[1,3],[1,4],[3,7]],
               ["root","abcd","cs","hello","etc","hello","solution"]))
print(solution(7,
               [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]],
               ["root", "a", "b", "c", "d", "efghij", "k"]))