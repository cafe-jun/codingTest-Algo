def solution(x, n):
    answer = []
    for i in range(1,n+1):
        print(i)
        answer.append(i*x)
    return answer


# print(solution(2,5))
# print(solution(4,3))
print(solution(-4,2))