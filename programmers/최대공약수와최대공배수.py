from math import gcd

# 너무 라이브러리를 이용했기 때문에 
def solution(n: int, m: int):
    return  [gcd(n,m),n * m // gcd(n,m)]

print(solution(3,12))