u = []
#f = open('test.txt')
#n, m = map(int, f.readline().split())
n, m = map(int, input().split())
for _ in range(n):
    #u.append(list(map(int, f.readline().split())))
    u.append(list(map(int, input().split())))
# f.close()
cnt = 0


def equal_compare(multA, multB):
    # 같을 경우
    isCheck = True
    #print(multA, ' ', multB, '비교')
    cnt = 0
    for i in range(m-1):
        for j in range(i, m):
            if value_compare(multA[i], multA[j], multB[i], multB[j]) == False:
                isCheck = False
                break
        if isCheck == False:
            break

    if isCheck == True:
        cnt += 1
    #print('결과', cnt)
    return cnt


def value_compare(a1, a2, b1, b2):
    if (a1 > a2 and b1 > b2) or (a1 == a2 and b1 == b2) or (a1 < a2 and b1 < b2):
        return True
    return False


for i in range(n-1):
    for j in range(i+1, n):
        #print(i+1, '우주', j+1, '우주 비교')
        cnt += equal_compare(u[i], u[j])

print(cnt)
