

def solution(numbers:list[int], hand:str):
    answer = ''
    keypad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    keys = dict()
    for i,v in enumerate(keypad):
        for j,k in enumerate(v):
            keys[k] = [i+1,j+1]

    l_hand = keys['*']
    r_hand = keys['#']          
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            l_hand = keys[num]
        elif num in [3, 6, 9]:
            answer += 'R'
            r_hand = keys[num]
        else:
            # 양옆에 동일한 걸리라면 주로 사용한 손을 사용하여 누른다 
            # 거리 먼저 계산 
            l_move = 0
            r_move = 0
            l_move += abs(keys[num][1]-l_hand[1])
            l_move += abs(keys[num][0]-l_hand[0])    
            r_move += abs(keys[num][1]-r_hand[1])
            r_move += abs(keys[num][0]-r_hand[0])
            if l_move == r_move:
                # 왼손잡이 
                if hand == 'left':
                    answer += 'L'
                    l_hand = keys[num]
                else:
                # 오른손잡이 
                    answer += 'R'
                    r_hand = keys[num]
            # 나머지는 거리계산후 가까운 거리손으로 누르기 
            # 3보다 크면 아래로 간다 
            elif l_move < r_move: 
                answer += 'L'
                l_hand = keys[num]
            elif l_move > r_move: 
                answer += 'R'
                r_hand = keys[num]
    return answer
    
    
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right") == "LRLLLRLLRRL")
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left") == "LRLLRRLLLRR")
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],"right") == "LLRLLRLLRL")