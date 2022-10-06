# 어디가 문제인지 다시한번 찾아보자 
# n-lef < x < right -n 의 범위에 대한 규칙을 꼭 찾아야한다 


def solution(n, left, right):
    answer = []
    move = left
    while move <= right:
        cycle,rest = divmod(move,n)
        for i in range(rest,n):
            if move > right:
                break
            if i <= (cycle):
                answer.append(cycle+1)
            else:
                answer.append((cycle+1)+(i-cycle))
            move += 1
    return answer


print(solution(4,7,15) == [4,3,3,3,4,4,4,4,4])
print(solution(3,4,8) == [2,3,3,3,3])
print(solution(3,2,5) == [3,2,2,3])
print(solution(4,6,14) == [3,4,3,3,3,4,4,4,4])
print(solution(4,7,14) == [4,3,3,3,4,4,4,4])
    #  answer = []
    # move = left
    # while move <= right:
    #     cycle,rest= divmod(move,n)
    #     for i in range(n):
    #         if i <= cycle:
    #             answer.append(cycle+1)
    #         else:
    #             temp_c,temp_r = divmod(move+i,n)
    #             answer.append((temp_c+1)+temp_r)          
    #     answer = answer[(move%n)-1:]
    #     move += (rest+1)
    #     while True:
    #         if move // n < right // n:
    #             cycle,rest = divmod(move,n)
    #             temp_c_before = [(cycle+1)]*(cycle+1)
    #             temp_c_after = [(cycle+1)+(i-(cycle)) for i in range(len(temp_c_before),n)] 
    #             temp_c_before.extend(temp_c_after)
    #             answer.extend(temp_c_before)
    #             move += n
    #         else:
    #             cycle,rest = divmod(right,n)
    #             for i in range(rest+1):
    #                 if i <= cycle:
    #                     answer.append(cycle+1)
    #                 else:
    #                     # i-cycle 거리  
    #                     answer.append((cycle+1)+(i-cycle))
    #             move += rest+1
    #             break