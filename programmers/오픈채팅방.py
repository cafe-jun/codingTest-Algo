from collections import deque


def solution(record: list[str]):
    answer = []
    # 룸을 해시로 표기 
    user_dict = dict()
    queue = deque()
    for r in record:
        type,user= r.split(' ',1)
        if type != 'Leave':    
            uid,nickname = user.split(' ')
            user_dict[uid] = nickname
            user = uid
        queue.append(type+' '+user)    
               
    while queue:
        message = queue.popleft()
        type,uid = message.split(' ',1)
        if type == 'Enter':
            output = user_dict[uid]+'님이 들어왔습니다.'
            answer.append(output)
        elif type == 'Leave':
            output = user_dict[uid]+'님이 나갔습니다.'
            answer.append(output)
      
    print(' ')  
    return answer



print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))