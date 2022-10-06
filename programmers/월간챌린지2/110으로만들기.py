from collections import deque
from inspect import stack


def solution(s: str):
    answer = []
    # 큐를 이용하여 110을 찾자
    for x in s:
        cnt = 0
        temp = []
        for c in x:
            if c == '0':
                if temp[-2:] == ['1', '1']:
                    cnt += 1
                    temp.pop()
                    temp.pop()
                else:
                    temp.append(c)
            else:
                temp.append(c)
        if cnt == 0:
            answer.append(x)
        # 110이 있다면
        else:
            final = deque()
            # 0이 나오기 전까지는 append
            while temp:
                if temp[-1] == '1':
                    final.append(temp.pop())
                elif temp[-1] == '0':
                    break

            # 0이 나왔다면 110을 주어진 count만큼 append
            while cnt > 0:
                final.appendleft('0')
                final.appendleft('1')
                final.appendleft('1')
                cnt -= 1

            # stack에 남아있는거 다 추가
            while temp:
                final.appendleft(temp.pop())
            answer.append(''.join(final))
    return answer


print(solution(["111100", "1110", "100111100", "0111111010"])
      == ["110110", "1101", "100110110", "0110110111"])
