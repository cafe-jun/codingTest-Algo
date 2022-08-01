

from collections import deque



def solution(board, skill):
    answer = 0
    # 영향을 받은 블록만 계산을 한다면 나머지는 상관이 없을듯 한데 .... 
    new_board = [[0 for _ in range(len(board[0])+1)] for _ in range(len(board)+1)]
    print(new_board)
    for sk in skill:
         type,r1,c1,r2,c2,degrees = sk
         # 누적합 
         value = degrees if type == 2 else (-1)*degrees
         new_board[r1][c1] += value 
         new_board[r1][c2+1] += (-1)*value
         new_board[r2+1][c1] += (-1)*value
         new_board[r2+1][c2+1] += value

    else:
        # 위에서 아래 
        for c in range(len(board[0])):
            for r in range(len(board)):
                new_board[r+1][c] += new_board[r][c]
        # 왼쪽에서 오른쪽 
        for r in range(len(board)):
            for c in range(len(board[0])):
                new_board[r][c+1] += new_board[r][c] 
       
        
                

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += new_board[i][j]
            if board[i][j] > 0:
                answer+= 1
    return answer


print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])==10)
print(solution([[1,2,3],[4,5,6],[7,8,9]],[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]])==6)

