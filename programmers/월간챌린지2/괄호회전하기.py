from collections import deque


def solution(s):
    answer = 0
    # 올바른 괄호 확인하기
    q = deque(list(s))
    # 회전 카운트
    cycle_cnt = 0
    # 큐를 이용하여 회전을 시켜보자
    while cycle_cnt < len(s):
        # queue 안에 문자열 JOIN 하기
        convert_s = ''.join(q)
        # 올바른 괄호인지 확인
        if correct_check(convert_s):
            # 올바른 괄호라면 카운트 올리기
            answer += 1
        # 괄호 문자열 회전
        q.append(q.popleft())
        # 회전 카운트 올리기
        cycle_cnt += 1
    return answer


def correct_check(s):
    # 체크 초기값 False
    check = False
    # stack 값 초기화
    stack = []
    # 괄호 array
    start_scope = ['(', '{', '[']
    for x in s:
        # stack 아무것도 없다면
        if not stack:
            # {([ 이라면 값 넣기
            if x in start_scope:
                # scope_dic[x] += 1
                stack.append(x)
                continue
            else:
                # 어떻게든 올바르지 못한 괄호
                return False
        # scope_dic에 key 가 있는 값인지 확인
        if x in start_scope:
            # stack 에 값을 넣기
            stack.append(x)
        else:
            # stack pop 하기
            value = stack[-1]
            # 각 괄호 별 체크
            if x == ')' and value == '(':
                stack.pop()
            elif x == ']' and value == '[':
                stack.pop()
            elif x == '}' and value == '{':
                stack.pop()
            else:
                break
    if not stack:
        check = True
    return check


print(solution("[](){}") == 3)
print(solution("}]()[{") == 2)
print(solution("[)(]") == 0)
print(solution("}}}") == 0)
print(solution("()(") == 0)
print(solution("(") == 0)
print(solution("{{{{{{") == 0)

# def correct_check(s):
#     # 체크 초기값 False
#     check = False
#     # stack 값 초기화
#     stack = []
#     # 괄호 dic
#     scope_dic = {"(": 0, "{": 0, "[": 0, }
#     for x in s:
#         # stack 아무것도 없다면
#         if not stack:
#             # {([ 이라면 값 넣기
#             if x in scope_dic.keys():
#                 scope_dic[x] += 1
#                 stack.append(x)
#                 continue
#             else:
#                 # 어떻게든 올바르지 못한 괄호
#                 return False
#         # scope_dic에 key 가 있는 값인지 확인
#         if x in scope_dic.keys():
#             # scope_dic count 올리기
#             scope_dic[x] += 1
#             # stack 에 값을 넣기
#             stack.append(x)
#         else:
#             # stack pop 하기
#             value = stack.pop()
#             # 각 괄호 별 체크
#             if x == ')' and value == '(':
#                 scope_dic['('] -= 1
#             elif x == ']' and value == '[':
#                 scope_dic['['] -= 1
#             elif x == '}' and value == '{':
#                 scope_dic['{'] += -1
#             else:
#                 break

#     for v in scope_dic.values():
#         if v != 0:
#             break
#     else:
#         check = True

#     return check
