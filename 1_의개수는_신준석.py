a,b,k = map(int,input().split())
a -= 1

dp = [0 for _ in range(len(str(b))+2)]

dp[0] = 0

if k == 0 :
    dp[1] = 1
    dp[2] = 10
    for i in range(3,len(str(b))+2):
        # print(int(str('1'*(i-2))+str('0')))
        result = (dp[i-1]+int(str('1'*(i-2))+str('0')))*9 + dp[i-1]
        dp[i] = result
else:     
    for i in range(1,len(str(b))+2):
        result = dp[i-1]*9+(10**(i-1)+dp[i-1])
        dp[i] = result

# 0 의 개수 
#  [0,1,10,190,2890,38890]
#  n = 2 => 10=(1+0)* 9 + 1
#  n = 3 => 180=(10+10)*9 + 10
#  n = 4 => 300=(190+ 110) * 9 + 190
#  n = 5 => 4000=(2890+1110) * 9 + 2890  36000+2890 388890 
#  n = 6 => 50000=(38890+11110)*9 + 

# dp[n] = (dp[n-1]+)*9 + dp[n-1]

# 0 10 110 1110 11110 10**(n-2)+10

def result_count(value) :
    count = 0
    value_list = str(value)
    value_len = len(value_list)
    for i, num in enumerate(value_list):
        for j in range(10):
            if j > int(num):
                break
            if k == 0 and i == 0:
                break; 
            if j <= int(num)-1:
                if j == k:
                    m = value_list[i+1:]
                    count += 10**(value_len-1-i) + dp[value_len-1-i]
                else:
                    count += dp[value_len-1-i]
            else:
                if j ==  k:
                    m = value_list[i+1:]
                    if m == '':
                        m = 0
                    count += int(m)+1
            # count 확인용 print(count)
    return count

if a == -1:
    print(result_count(b))
else:
    print(result_count(b))
    print(result_count(a))
    print(result_count(b)-result_count(a))
