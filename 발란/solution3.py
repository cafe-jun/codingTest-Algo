def solution(n):
    length = 0
    digit = 1

    while True:
        start = pow(10, digit - 1)
        end = pow(10, digit)

        # 현재 자릿수의 모든 경우의 수 계산
        count = ((end - start) * digit)

        # 현재 자릿수까지 포함된 모든 경우의 수가 n보다 작거나 같으면 다음 단계 진행 
        if length + count < n:
            length += count 
            digit += 1 
        else:
            break 

    # 현재 범위 내에서 몇 번째인 지 계산 
    index = (n - length - 1) // digit 
    number_in_position = (n - length - 1) % digit 

    # 해당 숫자를 문자열로 변환 후 위치에 따른 숫자 반환
    return int(str(start + index)[number_in_position])

print(solution(5))
print(solution(15))
