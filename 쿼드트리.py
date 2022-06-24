def solution(arr: list[list]):
    answer = []
    arr_len = len(arr)
    arr_step = arr_len // 2
    def quert_tree(arr):
        #print("전체 Array")
        #printArr(arr)
        result = [0,0]
        # 개수 세기 
        e_cnt = element_count(arr)
        #print("e_cnt : " + str(e_cnt))
        if e_cnt[0] == 0:
            return [0,1]
        if e_cnt[1] == 0:
            return [1,0]
        for i in range(0,len(arr[0]),len(arr[0])//2):
            for j in range(0,len(arr[0]),len(arr[0])//2):
                quert_arr = [a[j:j+len(a)//2] for a in arr[i:i+len(arr)//2]]
                quert_result = quert_tree(quert_arr)
                #print('quert_result')
                #print(quert_result)
                result[0] += quert_result[0]
                result[1] += quert_result[1]

        return result 
    
    answer = quert_tree(arr)
    #print('total:' + str(answer))
    return answer


def element_count(arr:list[list]):
    # return [zero_cnt,one_cnt]
    zero_cnt = 0
    one_cnt = 0
    for a in arr:
        zero_cnt += a.count(0)
        one_cnt += a.count(1)    
    return [zero_cnt,one_cnt]
        

def printArr(arr):
    for a in arr:
        print(a)
    print('=================')
print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]) == [4,9])
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]])==[10,15])
      