from locale import currency


def solution(n, m, x, y, queries):
    dn = [0, 0, -1, 1]
    dm = [-1, 1, 0, 0]
    answer = 0
    last_query = queries[-1]
    last_n = x-dn[last_query[0]]
    last_m = y-dm[last_query[0]]
    print(last_n, last_m)
    # for i in range(n):
    #     for j in range(m):
    #         # i,n 가 행 j,m 가 열
    #         current = [i, j]
    #         for query in queries:
    #             kn = dn[query[0]]*query[1] + current[0]
    #             km = dm[query[0]]*query[1] + current[1]
    #             if query[0] <= 1:
    #                 if 0 > km:
    #                     current[1] = 0
    #                 elif km >= m:
    #                     current[1] = m-1
    #                 else:
    #                     current[1] = km
    #             else:
    #                 if 0 > kn:
    #                     current[0] = 0
    #                 elif kn >= n:
    #                     current[0] = n-1
    #                 else:
    #                     current[0] = kn

    #             #print('move point: ', current)
    #         #print('finish point: ', current)
    #         if current[0] == x and current[1] == y:
    #             answer += 1
    # print(answer)
    return answer


print(solution(2, 2, 0, 0, [[2, 1], [0, 1], [1, 1], [0, 1], [2, 1]]) == 4)
print(solution(2, 5, 0, 1,	[[3, 1], [2, 2],
      [1, 1], [2, 3], [0, 1], [2, 1]]) == 2)
