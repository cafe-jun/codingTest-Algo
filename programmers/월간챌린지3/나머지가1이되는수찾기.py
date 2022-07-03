import math


def solution(n):
    answer = 0
    for i in range(2,n):
        #print(i,':',divmod((n-1),i))
        if (n-1)%i == 0:
            answer = i
            break
    else:
        answer = i
    return answer

print(solution(10) == 3)
print(solution(12) == 11)