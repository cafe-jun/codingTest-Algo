
from pydoc import cli


def solution(N, S:str):
    # write your code in Python 3.8.10
    answer = 0
    layer_dic = {'A': [0,0],'B': [0,1],'C': [0,2],'D': [1,0],'E': [1,1],'F': [1,2],'G': [1,3],'H': [2,0],'J': [2,1],'K': [2,2]}
    airplane_seat = []
    # 0 층 공백
    airplane_seat.append([])
    for _ in range(N):
        airplane_seat.append([[0,0,0],[0,0,0,0],[0,0,0]])
    for s in S.split(' '):
        if s != '':
            layer = s[-1]
            floor = int(s[:-1])
            airplane_seat[floor][layer_dic[layer][0]][layer_dic[layer][1]] = 1
    
    for i,seat in enumerate(airplane_seat):
        if i == 0:
            continue
        if seat[0][1] == seat[0][2] == seat[1][0] == seat[1][1] == 0:
            airplane_seat[i][0][1],airplane_seat[i][0][2],airplane_seat[i][1][0],airplane_seat[i][1][1] = 1,1,1,1 
            answer += 1
        if seat[1][0] == seat[1][1] == seat[1][2] == seat[1][3] == 0:
            airplane_seat[i][1][0],airplane_seat[i][1][1],airplane_seat[i][1][2],airplane_seat[i][1][3] = 1,1,1,1 
            answer += 1
        if seat[1][2] == seat[1][3] == seat[2][0] == seat[2][1] == 0:
            airplane_seat[i][1][2],airplane_seat[i][1][3],airplane_seat[i][2][0],airplane_seat[i][2][1] = 1,1,1,1 
            answer += 1      
    return answer

print(solution(2,"1A 2F 1C"))
print(solution(1," "))
print(solution(22,"1A 3C 2B 20G 5A"))
