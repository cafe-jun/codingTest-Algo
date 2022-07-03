def solution(s: str):
    answer = []
    s = s[1:-1]
    temp = []
    # 2자리 이상숫자면 어떻게 구성을 해야할까 ? 
    idx = 0
    t = ''
    while len(s) > idx:
        if t == '1234':
            break;
        t = ''
        if s[idx] == '{':
            t = s.index('}',idx)
            print(s[idx+1:t])
            temp.append(list(map(int,s[idx+1:t].split(','))))
            idx = t
        idx +=1
    temp = sorted(temp, key=lambda x : len(x))
    temp_list = []
    for t in temp:
        for m in t:
            if m not in temp_list:
                temp_list.append(m)
        
    answer = temp_list
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}") == [2, 1, 3, 4])
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}") == [2, 1, 3, 4])
print(solution("{{20,111},{111}}") == [111, 20])
print(solution("{{123}}") == [123])
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")== [3, 2, 4, 1])