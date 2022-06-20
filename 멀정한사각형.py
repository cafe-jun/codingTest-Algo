from math import gcd
def solution(w,h):
    answer = (w*h) - (w+h-gcd(w,h))
    return answer

print(solution(8,12))
