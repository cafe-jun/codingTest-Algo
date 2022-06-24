def solution(numbers):
    answer = []
    for num in numbers:
        diff_cnt = 1e9
        num_bit = convert_bit(num)
        # print('num : '+str(num) + ' sixteen:  '+num_sixteen_bit)
        compare_num = num
        compare_bit = num_bit
        
        while True:
            compare_num += 1
            # 최초로 0이 나오는 지점 칮기 
            for i in reversed(range(len(compare_bit))):
                if compare_bit[i] == '0':
                    compare_str_array = list(compare_bit)
                    compare_str_array[i] = '1'
                    if len(compare_bit[i+1:]) >0:
                        for j in range(i+1,len(compare_bit)):
                            compare_str_array[j] = '0'
                    compare_bit = ''.join(compare_str_array)
                    break
            else:
                compare_bit= '1'+('0'*len(compare_bit))
            #print('compare_num :'+str(compare_num)+'=>'+compare_bit)
            is_check = is_bit_diff_compare(compare_bit,num_bit)
            if is_check:
                break;
            # print('compare_bit : '+str(compare_bit) + ' diff_cnt:  '+str(diff_cnt))
        answer.append(compare_num)
    return answer

def is_bit_diff_compare (str1,str2):
    is_check = True
    diff_cnt= 0
    if len(str1) > len(str2):
            str2 = '0'+str2
    if len(str1) >= len(str2):
        for i in range(len(str2)):
            if str1[i] != str2[i]:
                diff_cnt += 1
            if diff_cnt >= 3:
                is_check = False
                break
    else:
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                diff_cnt += 1
            if diff_cnt >= 3:
                is_check = False
                break
    return is_check
def convert_bit(number):
    result = ''
    if number == 0:
        return '0'
    if number == 1:
        return '1' 
    while number > 1:
        result = str((number % 2)) + result
        number = number // 2
    return '1'+result
print(solution([1001,337,0,1,333,673,343,221,898,997,121,1015,665,779,891,421,222,256,512,128,100])== [1002, 338, 1, 2, 334, 674, 347, 222, 899, 998, 122, 1019, 666, 781, 893, 422, 223, 257, 513, 129, 101])
print(solution([0,2,7])==[1, 3, 11])





    