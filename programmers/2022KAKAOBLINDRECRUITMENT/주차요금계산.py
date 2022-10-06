# 기본시간(분)	 기본요금(원)	단위 시간(분)	단위 요금(원)
#   180	         5000	      10	      600
from collections import defaultdict

# 같은 시각에, 같은 차량번호의 내역이 2번 이상 나타내지 않습니다.
# 마지막 시각(23:59)에 입차되는 경우는 입력으로 주어지지 않습니다.
# 아래의 예를 포함하여, 잘못된 입력은 주어지지 않습니다.
# 주차장에 없는 차량이 출차되는 경우
# 주차장에 이미 있는 차량(차량번호가 같은 차량)이 다시 입차되는 경우

def solution(fees:list[int], records:list[str]):
    answer = []
    basic_m,basic_fee,add_minute,add_charge = fees
    fees_minute = defaultdict(int)
    park_state = dict()
    
    for record in records:
        time,fee,state = record.split(' ')
        if state == 'IN':
            park_state[fee] = time 
        elif state == 'OUT':
            stime = park_state[fee]
            # 실제로 빼고 
            interval = time_calculator(stime,time)
            fees_minute[fee] += interval
            del park_state[fee]
            
    else:
        # 출차가 안된 경우 
        if park_state.keys():
            for fees in park_state.keys():
                stime = park_state[fees]
                interval = time_calculator(stime,'23:59')
                fees_minute[fees] += interval
       
    #5000 + ⌈(334 - 180) / 10⌉ x 600 
    sort_fees= sorted(fees_minute.keys())
    
    for fminute in sort_fees:
        # 기본 요금 
        money = basic_fee
        basic_minute = fees_minute[fminute] - basic_m
        if basic_minute > 0:
            t = divmod(basic_minute,add_minute)
            money+= (t[0]*add_charge)
            if t[1] > 0:
                money += add_charge
        answer.append(money)
    print(answer)
    return answer

def time_calculator(stime: str,etime:str):
    # 모든걸분으로 변경하자 
    shour,sminute = stime.split(':')
    ehour,eminute = etime.split(':')
    sm = (int(shour)*60)+int(sminute)
    em = (int(ehour)*60)+int(eminute)
    return em - sm
    

print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])==[14600, 34400, 5000])
print(solution([120, 0, 60, 591],["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]) ==[0, 591])
print(solution([1, 461, 1, 10],["00:00 1234 IN"]) ==[14841])