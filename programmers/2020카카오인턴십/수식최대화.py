from collections import deque
from itertools import permutations


def solution(expression):
    answer = 0
    temp = []
    oper = set()
    t = ''
    for e in expression:
        if e == '*' or e == '+' or e == '-':
            oper.add(e)
            temp.append(int(t))
            temp.append(e)
            t = ''
        else:
            t += e
    else:
        temp.append(int(t))
    oper_list = list(oper)
    cnt = 0
    max_num = 0
    for opers in permutations(oper_list):
        stack = []
        temp_q = deque(temp)    
        for op in list(opers):
            while temp_q:
                v = temp_q.popleft()
                if op == v:
                    next = temp_q.popleft()
                    if op == '+':
                        stack.append(stack.pop() + next)
                    elif op == '-':
                        stack.append(stack.pop() - next)
                    elif op == '*':
                        stack.append(stack.pop() * next)
                else:
                    stack.append(v)
            for i in stack:
                temp_q.append(i)
            stack.clear()       
        max_num = max(max_num,abs(temp_q.popleft()))    
        cnt += 1  
    answer = max_num
    return answer

print(solution("177-661*999*99-133+221+334+555-166-144-551-166*166-166*166-133*88*55-11*4+55*888*454*12+11-66+444*99") == 6083974714)
print(solution("200-300-500-600*40+500+500") ==1248000)
print(solution("2*2*2*2*2-2*2*2") == 24)
print(solution("100-200*300-500+20") == 60420)
print(solution("50*6-3*2") == 300)


# from collections import deque


# def solution(expression):
#     answer = 0
#     temp = []
#     oper = set()
#     t = ''
#     for e in expression:
#         if e == '*' or e == '+' or e == '-':
#             oper.add(e)
#             temp.append(int(t))
#             temp.append(e)
#             t = ''
#         else:
#             t += e
#     else:
#         temp.append(int(t))
#     oper_list = list(oper)
#     cnt = 0
#     max_num = 0
#     while cnt < len(oper_list):
#         stack = []
#         temp_q = deque(temp)    
#         for op in oper_list:     
#             while temp_q:
#                 v = temp_q.popleft()
#                 if op == v:
#                     next = temp_q.popleft()
#                     if op == '+':
#                         stack.append(stack.pop() + next)
#                     elif op == '-':
#                         stack.append(stack.pop() - next)
#                     elif op == '*':
#                         stack.append(stack.pop() * next)
#                 else:
#                     stack.append(v)
#             for i in stack:
#                 temp_q.append(i)
#             stack.clear()
#         max_num = max(max_num,abs(temp_q.popleft()))    
#         oper_list.append(oper_list.pop(0))
#         cnt += 1  
#     answer = max_num
#     print(answer)
#     return answer