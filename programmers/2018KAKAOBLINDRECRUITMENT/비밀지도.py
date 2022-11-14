def solution(n: int, arr1 :list, arr2:list):
    answer = []
    for idx in range(len(arr1)):
        bin1 = bin(arr1[idx])[2:].rjust(n,'0')
        bin2 = bin(arr2[idx])[2:].rjust(n,'0')
        tmp = ''
        for j in range(n):
            num = int(bin1[j]) | int(bin2[j])
            if num == 1:
                tmp += '#'
            else:
                tmp += ' '
                
        answer.append(tmp)
    return answer


print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28])==["#####","# # #","### #","#  ##","#####"])
print(solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10])==["######","###  #","##  ##"," #### "," #####","### # "])
