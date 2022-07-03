# f = open('test.txt')
# n = int(f.readline())
# A = list(map(int, f.readline().split()))
# B = list(map(int, f.readline().split()))
# f.close()

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
answer = 0
dp = [0] * n
# 이미 더한걸 또 더할 필요가 있나 ?
sum_a = 0
sum_b = 0
before = 0
for i in range(n):
    sum_a = A[i]+sum_a
    sum_b = B[i]+sum_b
    if sum_a == sum_b or A[i] == B[i]:
        dp[i] = before + 1
        before = dp[i]
        sum_a = 0
        sum_b = 0
    else:
        if before > 0:
            before -= 1

answer = sum(dp)
print(answer)
