
from copy import copy


def solution(sticker:list[int]):
    answer = 0
    if len(sticker) <=3 :
        return max(sticker)
    max_sum = 0
    for k in range(2):    
        dp = [0] * len(sticker)
        if k == 1:
            dp[0] = 0
        else:
            dp[0] = sticker[0]
        dp[1] = sticker[1]
        for i in range(2,len(dp)-1+k):
            dp[i] = max(dp[i-1],dp[i-2]+sticker[i])
        else:
            max_sum = max(dp)
        answer = max(max_sum,answer)
    return answer

print(solution([5, 1, 16, 17, 16]))
print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
print(solution([1, 3, 2, 5, 10]))