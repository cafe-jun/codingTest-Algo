



n = int(input())
dp = [[],[]]
dp[1] = [(1,'A','B'),(1,'B','C')]

def moveHanoi(n,X,Y):
    return str(n)+' : '+X+'->'+Y
    

for i in range(2,n+1):
    dp[i%2].clear()
    for j in dp[(i-1)%2]:
        dp[i%2].append(((j[0],j[1],j[2])))
    dp[i%2].append(((i,'A','B')))
    for j in reversed(dp[(i-1)%2]):
        dp[i%2].append((j[0],j[2],j[1]))
    dp[i%2].append(((i,'B','C')))
    for j in dp[(i-1)%2]:
        dp[i%2].append(j)

for i in dp[n%2]:
    print(moveHanoi(i[0],i[1],i[2]))
print(len(dp[n%2]))

# def hanoi (n,start,end,other):
#     if n == 0:
#         return 
#     hanoi(n-1,start,end,other)
#     print(n,' : ',start,'->',end)
#     #  거꾸로
#     hanoi(n-1,other,end,start)
#     print(n,' : ',end,'->',other)
#     hanoi(n-1,start,end,other)
        
    
# hanoi(n,'A','B','C')
# [1]
# 1: A -> B
# 1: B -> C
# [2]
# --1
# 1: A -> B
# 1: B -> C 
# ----------------------------------------------------------------
# 2: A -> B
# 1: C -> B
# 1: B -> A
# 2: B -> C
# ----------------------------------------------------------------
# --1 
# 1: A -> B
# 1: B -> C


# [3]
# --1
# 1: A -> B
# 1: B -> C 
# ----------------------------------------------------------------
# 2: A -> B
# 1: C -> B
# 1: C -> A
# 2: B -> C
# ----------------------------------------------------------------
# --1 
# 1: A -> B
# 1: B -> C

