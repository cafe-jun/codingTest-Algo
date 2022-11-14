
from itertools import permutations


def solution(N, number):
    answer = 0
    # 0도 포함이기 때문 
    dp = [[] for _ in range(9)] 
    # 최소 개수는 자신 빼기 자신 
    dp[1] = [N]
    dp[2] = [int(str(N)+str(N)),N+N,N-N,int(N/N),N*N]
        
    print('')
    for i in range(3,9):
        for j in combi_list(i):
            for k in dp[j[0]]:
                for q in dp[j[1]]:
                    print(k,' ',q)
                    dp[i].append(int(str(k)+str(q)))
                    dp[i].append(k+q)
                    dp[i].append(k-q)
                    dp[i].append(k*q)
                    if q == 0:
                        dp[i].append(0)
                    else:
                        dp[i].append(k/q)
                
    
    print('')
    return answer

def combi_list(number):
    return [[i,number-i] for i in range(1,number)]

# print(solution(5,12))
print(solution(2,11))
# if j == 0:
            #     result = dp[j]+N 
            # elif j == 1:
            #     result = dp[j]-N 
            # elif j == 2:
            #     result = dp[j]*N 
            # elif j == 3:
            #     result = dp[j]/N
            # if result == i:
            #     dp[i] = min(dp[j]+1,dp[i])


# # 정수 N, M을 입력 받기
# n, m = map(int, input().split())
# # N개의 화폐 단위 정보를 입력 받기
# array = []
# for i in range(n):
#     array.append(int(input()))

# # 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
# d = [10001] * (m + 1)

# # 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
# d[0] = 0
# for i in range(n):
#     for j in range(array[i], m + 1):
#         print('array[i]', array[i])
#         print('j - array[i]',j - array[i])
#         print('d[j - array[i]',d[j - array[i]])
#         if d[j - array[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
#             d[j] = min(d[j], d[j - array[i]] + 1)

# # 계산된 결과 출력
# if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
#     print(-1)
# else:
#     print(d[m])
