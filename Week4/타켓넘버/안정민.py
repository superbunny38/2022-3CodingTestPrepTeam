from collections import deque

def solution(numbers, target):
    answer = 0
    # 2^20 = 1_000_000
    
    # answer = dfs(0, 0, target, numbers)
    answer = traversal(numbers, target)
    return answer

def dfs(idx, currSum, target, numbers):
    ways = 0
    
    if idx == len(numbers):
        return 1 if currSum == target else 0
    
    num = numbers[idx]
    ways += dfs(idx + 1, target, currSum + num, numbers) + dfs(idx + 1, target, currSum - num, numbers)
        
    return ways

def traversal(numbers, target) -> int:
    prevList = [0]
    for num in numbers:
        prevList = list(map(lambda x: x + num, prevList)) + list(map(lambda x: x - num, prevList))
        
    return prevList.count(target)