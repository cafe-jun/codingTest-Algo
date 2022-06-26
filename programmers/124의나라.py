from locale import nl_langinfo


def solution(n):
    answer = ''
    # 진법을 생각해서 나누는 방식으로 문제를 푼면 된다 
    # 문제는 나머지가 0일때인데 나머지가 0일때는 현재 n에 -1을 하여 다 마무리한것이 아닌 
    # n-1 째 까지 돌고 마지막 나머지라는점을 명확하게 하지 
    num_list = [4,1,2]
    while n > 0 :
        n,num_idx = divmod (n,3)
        # 나머지가 n 일때 
        if num_idx == 0:
            answer = str(num_list[num_idx]) +answer 
            # n-1 째 까지 돌고 마지막 나머지라는점을 명확하게 체크 
            n-=1
        else:
            answer =  str(num_list[num_idx])+ answer   
    return answer

print(solution(1))
print(solution(3))
print(solution(4))
print(solution(11))
print(solution(100))