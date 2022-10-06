import heapq

N, K = map(int, input().split())
A = list(map(int, input().split()))
P = list(map(int, input().split()))


# f = open('test.txt')
# N, K = map(int, f.readline().split())
# A = list(map(int, f.readline().split()))
# P = list(map(int, f.readline().split()))
# f.close()
# 이미 방문한 마을 t

# 공격력에 적고 최대한 많은 주민을 해방한다

houses = []
for i in range(N):
    heapq.heappush(houses, (A[i], -1*(P[i])))

t = []
answer = 0
while houses:
    value = heapq.heappop(houses)
    a, p = value
    t.append(a)
    if K < sum(t):
        break
    else:
        answer += (-1*(p))
    K -= sum(t)
print(answer)
