def solution(numbers :list[int], target: int):
    answer = 0
    def dfs(num,idx):
        result = 0
        if len(numbers)-1 == idx:
            if num == target:
                return 1
            else:
                return 0
        print("num = "+str(num)+" idx ="+str(idx))
        result += dfs(num + numbers[idx+1],idx+1)
        result += dfs(num +(-1*numbers[idx+1]),idx+1)    
        return result
    
    answer += dfs(numbers[0],0)
    answer += dfs((-1*numbers[0]),0)   
    return answer




print(solution([1, 1, 1, 1, 1],3))
print(solution([4, 1, 2, 1],4))