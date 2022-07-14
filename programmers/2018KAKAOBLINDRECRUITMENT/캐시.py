from collections import deque


def solution(cacheSize: int, cities: list[str]):
    answer = 0
    cacahe = []
    q = deque(cities)
    time = 0
    while q:
        city = q.popleft().upper()
        if city not in cacahe:
            cacahe.append(city)
            if len(cacahe) > cacheSize:
                cacahe.pop(0)
            time += 5
        else:
            hit_data = cacahe.pop(cacahe.index(city))
            cacahe.append(hit_data)
            time += 1
    answer = time
    return answer


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork",
      "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]) == 50)
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju",
      "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]) == 21)
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
      "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]) == 60)
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
      "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]) == 52)
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]) == 16)
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]) == 25)
