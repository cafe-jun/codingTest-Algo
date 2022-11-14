from collections import deque


# f = open('./BoJ/test.txt')

# T = int(f.readline())
T = int(input())
# N 세준 S
# M 세비 B
N_list = deque()
M_list = deque()
for tc in range(T):
    input()
    N_list.append(list(map(int, input().split())))
    M_list.append(list(map(int, input().split())))

    # f.readline()
    # N_list.append(list(map(int, f.readline().split())))
    # M_list.append(list(map(int, f.readline().split())))

# 전쟁은 여러 번의 전투로 이루어진다. 각 전투에서 살아있는 병사중 제일 약한 병사가 죽는다.
# 만약 제일 약한 병사가 여러 명이고, 제일 약한 병사가 모두 같은 편에 있다면,
# 그 중에 한 명이 임의로 선택되어 죽는다. 하지만, 제일 약한 병사가 여러 명이고,
# 양 편에 모두 있다면, 세비의 제일 약한 병사 중 한 명이 임의로 선택되어 죽는다.

for r in range(T):
    N = N_list.popleft()
    N = deque(sorted(N, reverse=True))
    M = M_list.popleft()
    M = deque(sorted(M))
    # 초기 세팅
    n = N.popleft()
    m = M.popleft()
    # 가장 약한 병사 출력
    while len(N) > 0 or len(M) > 0:
        # 세비의 승리 조건
        if n < m:
            print('B')
            break
    else:
        # 세비의 승리
        if n >= m:
            print('S')
        else:
            print('B')


# f.close()
