import sys
sys.setrecursionlimit(1000000)  
input = sys.stdin.readline


n,k = map(int,input().split())

def search(m):
    answer = 1e9
    if m == k:
        return 1
    if m+n < k+n:
        answer += min(search(m+n),answer)
    if m+1 < k:
        answer += min(search(m+1),answer)
    if m > k:
        answer += min(search(m-1),answer)
    return answer

print(int(search(n)//1e9))