
n = int(input())
triangles = []
for _ in range(n):
    triangles.append(list(map(int,input().split())))
    
# f = open('test.txt')
# n = int(f.readline())
# triangles = []
# for _ in range(n):
#     triangles.append(list(map(int,f.readline().split())))
# f.close()

for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            up_left = 0
        else:
            up_left = triangles[i-1][j-1]
        
        if i == j:
            up = 0
        else:
            up = triangles[i-1][j]
        triangles[i][j] = triangles[i][j] + max(up,up_left)
        
print(max(triangles[n-1]))
    