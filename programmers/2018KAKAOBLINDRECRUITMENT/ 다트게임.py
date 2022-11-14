def solution(dartResult):
    answer = 0
    score = {"S": 1, "D": 2, "T": 3}
    option = {"*": 2, "#": -1}
    tmp_list = []
    len_tmp = len(tmp_list)
    num = ''
<<<<<<< HEAD
    for idx, result in enumerate(dartResult):
        if result.isnumeric():
            num += result
        elif result in score.keys():
            # 숫자 끝 a
            tmp_list.append(int(num))
            num = ''
            tmp_list[-1] = tmp_list[-1] ** score[result]
            # 다트 연선이 끝인지 확인하기
            # if idx <= len_tmp:
            #     # 다음턴
            #     if result[idx+1].isnumeric():
            #         continue

            # else:
            #     continue
        else:
            if result == "*":
                # tmp_list 길이 확인
                if len(tmp_list) < 2:
                    tmp_list[0] = tmp_list[0]*option[result]
=======
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
>>>>>>> 4f999d12614bb37efb0ba6d666664ac34cdce520
                else:
                    tmp_list[-1] = tmp_list[-1]*option[result]
                    tmp_list[-2] = tmp_list[-2]*option[result]
            else:
                tmp_list[-1] = tmp_list[-1]*option[result]
<<<<<<< HEAD
=======
                
    return sum(tmp_list)
>>>>>>> 4f999d12614bb37efb0ba6d666664ac34cdce520

    return sum(tmp_list)
