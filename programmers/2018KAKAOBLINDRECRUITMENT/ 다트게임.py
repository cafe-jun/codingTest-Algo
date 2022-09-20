def solution(dartResult: str):
    answer = 0
    score = {"S": 1, "D": 2, "T": 3}
    option = {"*": 2, "#": -1}
    tmp_list = []
    idx = -1
    for result in dartResult:
        if result.isnumeric() == True:
            print('number')
            tmp_list.append(int(result))
            idx += 1
        elif result in score.keys():
            tmp_list[idx] += tmp_list[idx] ^ score[result]
        else:
            tmp_list[idx-1]*option[result]

    return answer


print(solution("1S2D*3T") == 37)
print(solution("1D2S#10S") == 9)
print(solution("1D2S0T") == 3)
print(solution("1S*2T*3S") == 23)
print(solution("1D#2S*3S") == 5)
print(solution("1T2D3D#") == -4)
print(solution("1D2S3T*") == 59)
