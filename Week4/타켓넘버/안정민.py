def solution(numbers, target):
    answer = 0
    # 2^20 = 1_000_000
    
    answer = dfs(0, 0, target, numbers)
    return answer

def dfs(idx, currSum, target, numbers):
    ways = 0
    
    if idx == len(numbers):
        return 1 if currSum == target else 0
    
    num = numbers[idx]
    ways += dfs(idx + 1, target, currSum + num, numbers) + dfs(idx + 1, target, currSum - num, numbers)
        
    return ways