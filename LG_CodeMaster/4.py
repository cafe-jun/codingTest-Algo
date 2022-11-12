import heapq
from itertools import permutations


def solution(marbles: list[int]):
    answer = [] 
    result = set()
    for r in range(1,len(marbles)+1):
        for marble in permutations(marbles,r):
            # 시소값 판단
            mar_list = []
            for mt in list(marble):
                mar_list.append(0)
                mar_list.append(mt)         
            for i in range(len(mar_list)):
                if sum(mar_list[:i]) == sum(mar_list[i+1:]):
                    if (len(mar_list[:i])-mar_list.count(0) ==len(mar_list[i:])-mar_list.count(0)):
                        result.add(marble)
                        break;
                
    else:
        
        suit2 = []
        for m in list(result):
            m_list = list(m)
            if len(suit2) == 0:
                suit2.append(m_list)
            else:
                if len(suit2[0]) < len(m):
                    suit2.clear()
                    suit2.append(m_list)
                elif len(suit2[0]) == len(m):
                    suit2.append(m_list)
        suit3 = []
        for s2 in suit2:
            if len(suit3) == 0:
                suit3.append(s2)
            else:
                if sum(suit3[0]) < sum(s2):
                    suit3.clear()
                    suit3.append(s2)
                elif sum(suit3[0]) == sum(s2):
                    suit3.append(s2)
        for s3 in suit3:
            heapq.heappush(answer,s3)  
    return answer[0]

print(solution([1,2,3,4,4])==[1,4,4,2,3])
print(solution([5,5,1,4])==[5,4,5])
print(solution([3,9,7,5])==[3,9,5,7])
print(solution([7,3,1])==[7])