import json
from collections import deque
import sys

f = open('./BoJ/test.txt')
n = int(f.readline())
# n = int(input())
command = []
arr = []
for _ in range(n): 
    # command.append(sys.stdin.readline().strip())
    # sys.stdin.readline()
    # arr.append(deque(json.loads(sys.stdin.readline().strip())))

    command.append(f.readline().strip())
    f.readline()
    arr.append(deque(json.loads(f.readline().strip())))
 
def solution(command: list[str],arr): 
    result = []   
    for i in range(n):
        cm = command[i]
        a = arr[i]
        isReverse = False 
        for c in cm:
            if c == 'R':
                isReverse = False if isReverse == True else True
            elif c == 'D':
                try:
                    if isReverse == False:
                        a.popleft()    
                    else:
                        a.pop()
                except IndexError:
                    print('error')
                    break
        else:
            if len(a) == 0:
                print('[]')
        
            else: 
                if isReverse == True:
                    a.reverse()
                print('[',end="")
                for j in range(len(a)-1):
                    print("%d,"%a[j],end="")
                print("%d]"%a[len(a)-1])


solution(command,arr)