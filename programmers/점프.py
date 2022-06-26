def solution(n):
    ans = 0
    # 순간이동은 지금까지의 온 거리의 2배 
    # 점프를 1반하면 건전지가 1씩 소모 
    # N 까지 가기위한 최소 소모 건전지 량 
    # 6 -> 3 -> 2 -> 1 -> 0 
    ans = back_tracking(n)
    return ans

def back_tracking(n):
    if n == 0:
        return 0;

    if n % 2 == 0:
        value = back_tracking(n // 2)
    else:
        value = back_tracking(n - 1)+ 1
    return value 
    
print(solution(5))
print(solution(6))
print(solution(5000))