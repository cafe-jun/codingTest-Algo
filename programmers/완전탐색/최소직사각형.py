from itertools import combinations


def solution(sizes):
    answer = 0

    max_v = 0
    max_h = 0
    for size in sizes:
        if size[0] < size[1]:
            max_v = max_v if max_v > size[1] else size[1] 
            max_h = max_h if max_h > size[0] else size[0] 
        else:
            max_v = max_v if max_v > size[0] else size[0] 
            max_h = max_h if max_h > size[1] else size[1] 
    else:
        answer = max_v * max_h
        
    
    # for c in combinations(list(size_set),2):
    #     for size in sizes:
    #         v = size[0]
    #         h = size[1]
    #         # 둘중 하나라도 만들수있으면 통과 
    #         if (v > c[0] or h > c[1]) and (h > c[0] or v > c[1]):
    #             break             
    #     else:
    #         if answer > c[0] * c[1]:
    #             answer = c[0] * c[1]     
    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]])== 4000)
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])== 120)
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])== 133)
