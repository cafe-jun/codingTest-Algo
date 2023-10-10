# def solution(n):
#     powers_of_three = [3**i for i in range(20)] # 충분히 큰 범위까지
#     possible_sums = {0}

#     for power in powers_of_three:
#         new_sums = {x + power for x in possible_sums}
#         possible_sums |= new_sums

#     sorted_sums = sorted(list(possible_sums))
    
#     return sorted_sums[n]

import heapq


def solution(n):
    result = 0
    power = 1
    
    while n > 0:
        result += (n % 2) * power
        n //= 2
        power *= 3
    
    return result
    

print(solution(4))
print(solution(11))