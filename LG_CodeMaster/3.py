def solution(reference,track):
    answer = 1e9
    # 부분 집합 생성 
    refer_list = []
    for i in range(1,len(reference)+1):
        for j in range(len(reference)+1-i):
            refer_list.append(reference[j:j+i])
    target = []
    index = 0
    while ''.join(target) != track:
        
        for i in range(len(track[index:])):
            print(track[index:index+i+1])
            if track[index:index+i+1] not in refer_list:
                target.append(track[index:index+i])
                index += i
                break;
        else:
            target.append(track[index:index+i+1])
        print(''.join(target))
        
    for i in target:
        answer = min(len(i),answer)
    return answer


# print(solution("abc","bcab")==2)
print(solution("vxrvip","xrviprvipvxrv") ==4)