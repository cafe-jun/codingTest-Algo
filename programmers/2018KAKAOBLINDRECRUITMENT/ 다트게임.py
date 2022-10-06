def solution(dartResult: str):
    answer = 0
    score = {"S": 1, "D": 2, "T": 3}
    option = {"*": 2, "#": -1}
    tmp_list = []
    len_tmp = len(tmp_list)
    num = ''
    for idx,result in enumerate(dartResult):
        if result.isnumeric():
            num += result
        elif result in score.keys():
            # 숫자 끝 
            tmp_list.append(int(num))
            num = ''
            tmp_list[-1] = tmp_list[-1] ** score[result]
        else:
            if result == "*":
            # tmp_list 길이 확인 
                if len(tmp_list) < 2:
                    tmp_list[0] =tmp_list[0]*option[result]
                else:
                    tmp_list[-1] = tmp_list[-1]*option[result]
                    tmp_list[-2] = tmp_list[-2]*option[result]
            else:
                tmp_list[-1] = tmp_list[-1]*option[result]
                
    return sum(tmp_list)

print(solution("1S2D*3T") == 37)
print(solution("1D2S#10S") == 9)
print(solution("1D2S0T") == 3)
print(solution("1S*2T*3S") == 23)
print(solution("1D#2S*3S") == 5)
print(solution("1T2D3D#") == -4)
print(solution("1D2S3T*") == 59)
