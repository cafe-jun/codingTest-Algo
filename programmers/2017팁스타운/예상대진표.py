def solution(n,a,b):
    answer = 0
    max_n = max(a,b)
    min_n = min(a,b)
    while check(max_n,min_n):
         # 붙기 
         # max_n 이 짝수면 2로 나누고 홀수면 +1한뒤 // 2 
         max_n = fight(max_n)
         min_n = fight(min_n)
         answer += 1
    else:
        answer += 1
    return answer

def check(max_n,min_n):
    # 큰쪽이 짝이고 작은쪽이 홀이고 큰 -1 != 작이 성립할때
    if max_n % 2 ==0 and max_n-1 == min_n and min_n % 2 == 1:
        return False;
    else:
        return True
        
def fight(n):
    return n // 2 if n%2 == 0 else (n+1)//2 

print(solution(8,4,7) ==3)
print(solution(8,2,3) ==2)
