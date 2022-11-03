
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def solution(A: list[int], B: list[int]):
    A.sort()
    B.sort(reverse=True)
    result = 0
    for i in range(len(A)):
        result += A[i]*B[i]
    return result


print(solution(A, B))
