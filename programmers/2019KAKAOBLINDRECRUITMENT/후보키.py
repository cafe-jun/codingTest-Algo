
from copy import copy
from itertools import combinations

# 잘푼 풀이를 찾아보자 
def solution(relation:list[str]):
    answer = 0
    global relations
    relations = copy(relation)
    for i in range(1,len(relations)+1):
        tmp = []
        for columns in combinations(range(len(relations[0])),i):
            if uniqueness(columns) == True:
                if len(columns) > 1:
                    if minimality_check(columns) == True:
                        tmp.append(True)
                    else:
                        tmp.append(False)
                else:
                    tmp.append(True)
            else:
                tmp.append(False)
        else:
            for t in tmp:
                if t == True:
                    answer += 1
    return answer
# 유일성 체크 
def uniqueness(columns: list[int]):
    tmp = []
    is_check = False
    for r in relations:
        tmp_list = [] 
        for c in columns:
            tmp_list.append(r[c])
        if tmp_list in tmp:
            break    
        tmp.append(tmp_list)
    else:
        is_check = True
    return is_check
    
# 최소성 체크 
def minimality_check(columns: list[int]):
    is_check = True
    for i in reversed(range(len(columns))):
        for c in combinations(list(columns),i):
            # 각 어떤것을 빼로 유일하게 식별이 되면 안된다 
            if uniqueness(list(c)) == True:
                is_check = False
                break
        if is_check == False:
            break
    return is_check
    # 나와 있는 컬럼중 한개씩 빼서 유일성을 만족하는지 확인 
print(solution([["100","100","ryan","music","2"], 
                ["200","200","tube","math","2"], 
                ["100","100","tube","computer","3"], 
                ["400","400","con","computer","4"],
                ["100","500","muzi","music","3"], 
                ["600","600","muzi","music","2"]])==5)
print(solution([["100","100","ryan","music","2"], 
                ["200","200","apeach","math","2"], 
                ["300","300","tube","computer","3"], 
                ["400","400","con","computer","4"],
                ["500","500","muzi","music","3"], 
                ["600","600","apeach","music","2"]])==3)
print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])==2)