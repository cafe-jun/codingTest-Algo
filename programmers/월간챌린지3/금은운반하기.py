def solution(a:int, b:int, g:list[int], s:list[int], w:list[int], t:list[int]):
    answer = 0

    # 이진 탐색으로 풀어보자 
    # 시작 start
    start = 1
    # 끝 end 
    end = 10e2*10e5*2*min(t)
    while start <= end:
        mid = (start + end) // 2
        max_resouce = 0 # t 시간동안 최대로 옮길 수 있는 자원의 양 
        max_g = 0
        max_s = 0
        for i in range(len(g)):
            x,y = divmod(mid,t[i])
            n,m = divmod(x,2)
            max_g += min((n+m)*w[i],g[i])
            max_s = min((n+m)*w[i],s[i])
            max_resouce += max(max_g,max_s)
        if max_resouce >= a+b and max_g >= a and max_s >= b:
            end = mid -1
            answer = mid
        else: 
            start = mid +1
    return int(answer)


print(solution(10,10,[100],[100],[7],[10]) ==50)
print(solution(90,500,[70,70,0],[0,0,500],[100,100,2],[4,8,1])==499)


    # 1번 케이스 
    # 도시가 오직 하나뿐이므로, 0번 도시의 유일한 트럭이 모든 운반을 해결해야 합니다. 이 트럭은 최대 7kg만큼의 광물을 운반할 수 있으며 편도 완주에는 10시간이 걸립니다.
    # 맨 처음에 10시간을 써서 7kg만큼의 금을 운반하고, 10시간을 써서 다시 도시로 돌아오고, 10시간을 써서 7kg만큼의 은을 운반하고, 10시간을 써서 다시 도시로 돌아오고, 마지막으로 10시간을 써서 3kg만큼의 금과 3kg만큼의 은을 운반하면, 총 50시간 만에 필요한 모든 금과 은을 조달할 수 있습니다.
    # 따라서, 50을 return 해야 합니다.
    
    # 2번 케이스 
    # 도시가 3개이고, 0번과 1번 도시는 금만 70kg씩 가지고 있고 2번 도시는 은을 500kg 가지고 있습니다.
    # 0번 도시의 트럭은 용량은 100kg, 편도 완주 시간은 4시간입니다.
    # 1번 도시의 트럭은 용량은 100kg, 편도 완주 시간은 8시간입니다.
    # 2번 도시의 트럭은 용량은 2kg, 편도 완주 시간은 1시간입니다.
    # 금은 0번 도시의 트럭과 1번 도시의 트럭이 각각 45kg씩 나누어서 운반하면 8시간 안에 필요한 모든 금을 조달할 수 있습니다.
    # 은은 2번 도시의 트럭이 한 번에 2kg씩 250번 운반하면(249번 왕복 + 1번 편도) 총 499시간 만에 필요한 모든 은을 조달할 수 있습니다.
    # 따라서, 499를 return 해야 합니다.
