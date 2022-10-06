

def solution(m: int, n:int, board: list[str]):
    answer = 0
    matrix = [list(s) for s in board]
    v = set()    
    while True:
        for i in range(m-1):
            for j in range(n-1):
                # 빈칸 체크 
                if matrix[i][j] == '0':
                    continue
                
                # 옆 아래 대삭선 체크 
                if matrix[i][j] == matrix[i][j+1] and matrix[i][j] == matrix[i+1][j] and matrix[i][j] == matrix[i+1][j+1]:
                    v.add((i,j))
                    v.add((i,j+1))
                    v.add((i+1,j))
                    v.add((i+1,j+1))
        
        v_list = list(v)
        answer += len(v_list)
        v.clear()
        if not v_list:
            break
        for b in v_list:
            i,j = b
            matrix[i][j] = '0'      
       # 위에있는 블록이 아래로 떨어지게함 
        for y in range(n):
            for x in reversed(range(m)):  
                if matrix[x][y] == '0':
                    for k in range(x-1,-1,-1):
                        if matrix[k][y] != '0':
                            matrix[x][y] = matrix[k][y]
                            matrix[k][y] = '0'
                            break
                    
                
    return answer
print(solution(4,4,["ABCD", "BACE", "BCDD", "BCDD"])==8)
print(solution(5,6,['AAAAAA','BBAATB','BBAATB','JJJTAA','JJJTAA']) ==24)
print(solution(2,2,["AA", "AA"])==4)
print(solution(2,2,["AA", "AB"])==0)
print(solution(3,2, ["AA", "AA", "AB"])==4)
print(solution(6,2, ["DD", "CC", "AA", "AA", "CC", "DD"])== 12)
print(solution(8,2, ["FF", "AA", "CC", "AA", "AA", "CC", "DD", "FF"])==8)
print(solution(6,2, ["AA", "AA", "CC", "AA", "AA", "DD"])==8)
print(solution(4,2, ["CC", "AA", "AA", "CC"]) == 8)
print(solution(4,5,["AAAAA","AUUUA","AUUAA","AAAAA"])==14)
print(solution(8,5,["HGNHU", "CRSHV", "UKHVL", "MJHQB", "GSHOT", "MQMJJ", "AGJKK", "QULKK"])== 8)
print(solution(4,4,["ABBA", "CBBC", "ABBA", "ABBA"])== 8)
print(solution(4,4,["ABBA", "ABBA", "AAAA", "AAAA"])== 12)
print(solution(4,4,["AAAA", "AABA", "AAAA", "AAAA"])== 12)
print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"])== 14)
print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]) ==15)
