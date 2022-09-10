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
    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]])== 4000)
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])== 120)
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])== 133)
