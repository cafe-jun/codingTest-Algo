from collections import defaultdict

answer = -1


def solution(info, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    def dfs(cur, sheep, wolf, next_set):
        sheep += info[cur] ^ 1
        wolf += info[cur]

        if sheep <= wolf:
            return
        if sheep > wolf:
            global answer
            answer = max(answer, sheep)
            for next_ in next_set:
                temp = set(graph.get(next_, []))
                next_set |= temp
                next_set -= set([next_])
                dfs(next_, sheep, wolf, next_set)
                next_set |= set([next_])
                next_set -= temp

    dfs(0, 0, 0, set(graph.get(0)))
    print(answer)
    return answer


print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [[0, 1], [1, 2], [1, 4], [
      0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]) == 5)
print(solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0], [[0, 1], [0, 2], [
      1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]) == 5)
