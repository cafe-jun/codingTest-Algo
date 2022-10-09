a,b = map(int,input().split())
a -= 1
b_len = len(str(b))
a_len = len(str(a))
dp = [0 for _ in range(b_len+1)]

for i in range(1,b_len+1):
    dp[i] = dp[i-1]*7 + (3*(dp[i-1]+10**(i-1)))

a_count =0 
b_count =0 

# def check(i,j,length,idx):
#     count = 0
#     if i <= j:
#         return count;
#     if i in [3,6,9]:
#         count += (dp[(length-1)-idx]+(10**(length-1-idx)))
#     else:    
#         count += dp[(length-1)-idx]

# 3이 두번이나 카운팅이 안됨 
for a_idx,a_i in enumerate(map(int,list(str(a)))):
    for a_j in range(10):
        if a_i < a_j:
            break;
        if a_j < a_i and a_j in [3,6,9]:
            if a_idx <= a_len-2:
                a_count += int(str(a)[a_len-2+a_idx:])+1 + dp[(a_len-1)-a_idx]
            else:
                a_count += 1
        else:         
            if a_j in [3,6,9]:
                if a_idx <= a_len-2:
                    a_count += int(str(a)[a_len-2+a_idx:])+1 #  0 포함해서 +1 추가 
                else:
                    a_count += 1
            else:    
                a_count += dp[(a_len-1)-a_idx]
for b_idx,b_i in enumerate(map(int,list(str(b)))):
    for b_j in range(10):
        if b_i < b_j:
            break;
        if b_j < b_i and b_j in [3,6,9]:
            if b_idx <= b_len-2:
                b_count += int(str(b)[b_len-2+b_idx:])+1 + dp[(b_len-1)-b_idx]
            else:
                b_count += 1
        else:         
            if b_j in [3,6,9]:
                if b_idx <= b_len-2:
                    b_count += int(str(b)[b_len-2+b_idx:])+1 #  0 포함해서 +1 추가 
                else:
                    b_count += 1
            else:    
                b_count += dp[(b_len-1)-b_idx]
   
print(b_count - a_count)