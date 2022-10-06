def solution(places):
    global matrix
    answer = []

    for place in places:
        matrix = [[c for c in s] for s in place]
        is_check = True
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == 'P':
                    # print(i,j,'검사')
                    # 왼쪽 검사
                    for l in range(1,3):
                        if 0<= j-l < 5:
                            if matrix[i][j-l] == 'P':
                                is_check = False
                                break
                            elif matrix[i][j-l] == 'X':
                                break
                            if l == 1 and 0<= i+1 < 5:
                                if matrix[i+1][j-1] == 'P':
                                    is_check = False
                                    break                    
                    if is_check ==False:
                        break;
                    # 아래쪽 검사 
                    for d in range(1,3):
                        if 0<= i+d < 5:
                            if matrix[i+d][j] == 'P':
                                is_check = False
                                break
                            elif matrix[i+d][j] == 'X':
                                break
                            if d == 1 and 0<=j-1<5:
                                if matrix[i+d][j-1] == 'P': 
                                    is_check = False
                                    break
                            if d == 1 and 0<=j+1<5:
                                if matrix[i+d][j+1] == 'P':
                                    is_check = False
                                    break
                    if is_check ==False:
                        break; 
                    # 오른쪽 검사 
                    for r in range(1,3):
                        if 0<= j+r < 5:
                            if matrix[i][j+r] == 'P':
                                is_check = False
                                break
                            elif matrix[i][j+r] == 'X':
                                break    
                            if r == 1 and 0<= i+1 < 5:
                                if matrix[i+1][j+1] == 'P':
                                    is_check = False
                                    break 
                    if is_check ==False:
                        break;
            if is_check ==False:
                break
        if is_check == True:
            answer.append(1)
        else:
            answer.append(0)
    # print(answer)
    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])==[1, 0, 1, 1, 1])