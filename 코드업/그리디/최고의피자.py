# https://codeup.kr/problem.php?id=3321

# N = int(input())
# A, B = map(int, input().split())
# A + k × B => 한 피자의 가격
#
f = open('./코드업/그리디/test.txt')

N = int(f.readline())
A, B = map(int, f.readline().split())
C = int(f.readline())
D = []
for i in range(N):
    D.append(int(f.readline()))

print('')
print('')
