n = input()
n_len = len(n)
r = 0
c = 1000
# 약수 구하기 
last = (n_len//2)+1
for i in range(1,last):
    x,y = divmod(n_len,i)
    if(y==0):
        if(i<=x):
           r = max(r,i);
           c = min(x,c)
index = 0
arr = [['0' for j in range(c)] for i in range(r)]
for i in range(c):
    for j in range(r):
        arr[j][i] = n[index]
        index += 1
result = ''
for i in range(r):
    result += ''.join(arr[i])
print(result)
