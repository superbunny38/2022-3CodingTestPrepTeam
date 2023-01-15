minCount = 9

def solution(N, number):
    dfs(0, 0, N, number)
    return minCount if minCount != 9 else -1

def dfs(cnt, num, unit, target):
    global minCount
    
    if cnt > 8 or cnt > minCount:
        return minCount
    
    if num == target:
        minCount = min(minCount, cnt)
        return minCount
    
    for i in range(1, 6):
        diff = int(str(unit) * i)
        dfs(cnt + i, num + diff, unit, target)
        dfs(cnt + i, num - diff, unit, target)
        dfs(cnt + i, num * diff, unit, target)
        dfs(cnt + i, num // diff, unit, target)
    