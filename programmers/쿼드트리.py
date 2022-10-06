def solution(arr: list[list]):
    answer = []
    up = arr[:len(arr)//2]
    down = arr[len(arr)//2:]
    print(up)
    print(down)
    # def quart(arr):
    #     print(arr)
    #     print(arr[:len(arr)/2][:len(arr)/2])
    #     one_quart = arr[:len(arr)/2][:len(arr)/2]
    return answer


print(solution([[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [
      0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1]]))
print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))
