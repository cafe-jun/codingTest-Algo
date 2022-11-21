
import math

N,M = map(int,input().split())
def solution(n,m):
    return m-math.gcd(n,m)
    
print(solution(N,M))
# print(solution(2,6)==4) 
# print(solution(3,4)==3) 
# print(solution(6,2)==0) 