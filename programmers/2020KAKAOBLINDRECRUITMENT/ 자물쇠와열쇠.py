from copy import deepcopy
from tabnanny import check


def solution(key, lock):
    answer = True
    # 배열 90도 회전하기 
    key_n = len(key)
    lock_n = len(lock)
    #lock 을 확장하기 
    new_lock = [[0 for _ in range(len(lock)*3)] for _ in range(len(lock)*3)]
    for i in range(len(lock)):
        for j in range(len(lock)):
            new_lock[i+len(lock)][j+len(lock)] = lock[i][j]
    # 90도 를 4번 
    is_check = False
    for _ in range(4):
        # key = rotation_2d(key)
        for i in range(key_n-1+lock_n):
            for j in range(key_n-1+lock_n):
                tmp_lock = deepcopy(new_lock)
                for k in range(key_n):
                    for m in range(key_n):
                        tmp_lock[i+k+len(lock)-(len(key)-1)][j+m+len(lock)-(len(key)-1)] += key[k][m]
                printArray(tmp_lock)
                if check_lock(tmp_lock,lock_n) == True:
                    is_check = True
                    printArray(key)
                    break
            if is_check == True:
                break
        if is_check == True:
            break
        key = rotation_2d(key)
    answer = is_check
    return answer

def check_lock(lock,n):
   is_check = True
   for i in range(n):
        for j in range(n):
            if lock[i+n][j+n] == 0 or lock[i+n][j+n] > 1:
                is_check= False
                break
        if is_check == False:
            break
   return is_check

def rotation_2d(key):
    n = len(key)
    new = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new[j][n-i-1] = key[i][j]
    return new

def printArray(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j],end=' ')
        print('\n')
        
print(solution([[1, 0], [0, 0]],[[1, 0, 0], [1, 0, 0], [1, 1, 1]])== False)
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]])==True)