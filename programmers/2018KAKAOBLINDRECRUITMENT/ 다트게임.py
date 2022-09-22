def solution(dartResult):
    answer = 0
    score = {"S": 1, "D": 2, "T": 3}
    option = {"*": 2, "#": -1}
    tmp_list = []
    len_tmp = len(tmp_list)
    num = ''
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
                else:
                    tmp_list[-1] = tmp_list[-1]*option[result]
                    tmp_list[-2] = tmp_list[-2]*option[result]
            else:
                tmp_list[-1] = tmp_list[-1]*option[result]

    return sum(tmp_list)
