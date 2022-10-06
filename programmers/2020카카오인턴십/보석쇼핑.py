from collections import defaultdict
import heapq
def solution(gems: list[str]):
    answer = []
    # 우선순위큐 : 데이터를 담을 temp array 생성 
    temp = []
    collected_gem = []
    collected_gem = defaultdict(int)
    # 최소 스타트 [0] => 보석이름,[1] => 보석 위치 
    
    min_start = ''
    for idx,gem in enumerate(gems):
        collected_gem[gem] = idx+1
        # 연속된 보석중 가장 앞에 있는 보석이 나올경우 
        if min_start == gem or min_start == '':
            # 누가 최소인지 찾기 
            min_num = 10e9
            # 이미 제일 앞에 있는 보석이 제일 뒤로 가서 가장 앞에 있는 보석의 순서를 찾아야 합니다.
            for c in collected_gem.items():
                if min_num > c[1]:
                    min_start = c[0]
                    min_num= c[1]
                # print("min_start update",min_start)       
        # 최소 거리 계산 
        distance = (idx+1)-collected_gem[min_start]
        # 가지고 있는 보석 개수 저장 
        gems_cnt = len(collected_gem.keys())
        # 시작 포인트 
        start_point = collected_gem[min_start]
        # 개수(큰수대로))거리(작은순),시작(작은순) 순으로 우선순위를 두고 우선순위 큐에 저장 
        group = ((-1)*gems_cnt,distance,start_point)
        if not temp:
            heapq.heappush(temp,((-1)*gems_cnt,distance,start_point))
        elif group != temp[0]:
            heapq.heappush(temp,((-1)*gems_cnt,distance,start_point))
    #print(temp[0])
    _,dist,start = heapq.heappop(temp)
    answer = [start,start+dist]
    return answer

print(solution(["A","B","B","B","B","B","B","C","B","A"])==[8,10])
print(solution(["A"])==[1,1])
print(solution(["A","A","A","B","B"])== [3,4])
print(solution(["AB","x","y","BD","e","AB","AC"])==[2, 7]);
print(solution(["AB","BD","AB","BD","BD","AB","AC"])==[5, 7]);
print(solution(["A", "A", "B"])==[2, 3]);
print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])==[3,7])
print(solution(["AA", "AB", "AC", "AA", "AC"])==[1, 3])
print(solution(["XYZ", "XYZ", "XYZ"])==[1, 1])
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])==[1, 5])
 
 