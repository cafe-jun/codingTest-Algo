n = int(input())
dp = [0 for i in range(3)]


# 점화식 a[n] = a[n-1] + a[n-2] + a[n-3]
if n == 1:
    print(1)
    exit()
elif n== 2:
    print(2)
    exit()
elif n == 3:
    print(4)
    exit()
else:
    dp[0] = 1
    dp[1] = 2
    dp[2] = 4
    for i in range(3,n):
        value = dp[(i-1)%3] + dp[(i-2)%3] + dp[(i-3)%3]
        dp[i%3] = value

print(dp[(n%3)-1]%1000)

