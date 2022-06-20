a, b = map(int, input().split())
a -= 1
dp = [0 for _ in range(len(str(b))+2)]
dp[0] = 0
dp[1] = 3

for i in range(2, len(str(b))+2):
    result = dp[i-1]*7+(10**(i-1)+dp[i-1])*3
    dp[i] = result

# b 박수 - a 박수
def result_count(value) :
    count = 0
    value_list = str(value)
    value_len = len(value_list)
    for i, num in enumerate(value_list):
        for j in range(10):
            if j > int(num):
                break
            if j <= int(num)-1:
                if j in [3, 6, 9]:
                    m = value_list[i+1:]
                    count += 10**(value_len-1-i) + dp[value_len-1-i]
                else:
                    count += dp[value_len-1-i]
            else:
                if j in [3, 6, 9]:
                    m = value_list[i+1:]
                    if m == '':
                        m = 0
                    count += int(m)+1
            # count 확인용 print(count)
    return count

print(result_count(b)-result_count(a))
