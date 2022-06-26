from hashlib import new


def one_step(new_id: str): # 대문자에서 소문자로 변경하기 
    return new_id.lower()

def two_step(new_id: str): 
    result = '' 
    for char in new_id: 
        if 'a' <= char <= 'z' or '0' <= char <= '9' or char == '-' or char == '_' or char == '.': 
            result += char 
    return result

def three_step(new_id: str): 
    while new_id.count('..') > 0:
        new_id = new_id.replace('..','.')
    return new_id
    
def four_step(new_id:str) :
    if new_id == '':
        return '';
    while new_id[0] == '.' or new_id[-1] == '.':
        # 문자열 길이가 0 일때 -1 이 됨 -1 아무것도 찾지 못할때 
        if new_id[0] == '.':
            new_id = new_id[1:]
        elif new_id[-1] == '.':
            new_id = new_id[:len(new_id)-1]
        if new_id == '':
            break             
    return new_id
        
def solution(new_id): 
    answer = '' 
    answer = one_step(new_id) 
    #print('1 step : ', answer) 
    answer = two_step(answer) 
    #print('2 step : ', answer) 
    answer = three_step(answer)
    #print('3 step : ', answer) 
    answer = four_step(answer)
    #print('4 step : ', answer) 
    # step 5
    if answer == '':
        answer = 'a'
    #print('5 step : ', answer) 
    if len(answer) >= 16:
        answer = answer[:15]
        
    #print('6 step : ', answer)
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]    
    #print('7 step : ', answer)
    return answer

print('result :',solution("...!@BaT#*..y.abcdefghijklm"),'expect : bat.y.abcdefghi')
print('result: ',solution('......a......a......a.....'),'expect : a.a.a')
print('result :',solution("z-+.^."),'expect : z--')
print('result :',solution("=.="),'expect : aaa')
print('result :',solution("123_.def"),'expect : 123_.def')
print('result :',solution("abcdefghijklmn.p"),'expect : abcdefghijklmn')
