def solution(n: int, t:int, m:int, p:int):
    answer = ''
    # 튜브가 말해야 하는 숫자 t개를 공백 없이 차례대로 나타낸 문자열. 단, 10~15는 각각 대문자 A~F로 출력한다.
    num = 0
    point = 1
    while len(answer) < t:
        convert_str = transformation(num,n)
        for c in convert_str:
            if (p % m) == (point % m):
                answer += c            
            point += 1
         # convert 끝날경우 한개 더 추가 
        num += 1
    answer = answer[:t]
    return answer
    
def transformation(num,q):
    if num == 0:
        return '0'
    rev_base = ''
    while num >0:
        num,mod = divmod(num,q)
        if mod >= 10:
            rev_base += chr(65+(mod % 10))
        else:
            rev_base += str(mod)
            
    return rev_base[::-1]
    

print(solution(2,4,2,1) == "0111")
print(solution(16,16,2,1) == "02468ACE11111111")
print(solution(16,16,2,2) == "13579BDF01234567")
