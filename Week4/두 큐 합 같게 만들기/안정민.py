from collections import deque

def solution(queue1, queue2):
    result = -1
    MAX_CNT = 4 * len(queue1)
    sum1, sum2 = sum(queue1), sum(queue2)
    
    if (sum1 + sum2) % 2 != 0:
        return result
        
    cnt = 0
    dq1, dq2 = deque(queue1), deque(queue2)
    while MAX_CNT > cnt:
        if sum1 == sum2:
            result = cnt
            break
            
        if sum1 > sum2:
            moved = dq1.popleft()
            dq2.append(moved)
            sum1 -= moved
            sum2 += moved
        else:
            moved = dq2.popleft()
            dq1.append(moved)
            sum2 -= moved
            sum1 += moved
        
        cnt += 1
    
    return result

def solution2(queue1, queue2):
    result = -1
    
    targetList = queue1 + queue2
    maxLen = len(targetList)
    
    totalSum = sum(targetList)
    if totalSum % 2 != 0:
        return result
    
    targetSum = totalSum // 2
    
    s = cnt = 0
    e = maxLen // 2 - 1
    currSum = sum(queue1)
    while s <= e and e < maxLen - 1:
        if currSum == targetSum:
            result = cnt
            break
        
        if currSum < targetSum:
            e += 1
            currSum += targetList[e]
        else:
            currSum -= targetList[s]
            s += 1
        
        cnt += 1
        
    return result

temp1 = [1, 2, 3, 5, 3, 1]
temp2 = [4, 5, 8, 2, 10, 2]

print(solution(temp1, temp2))
print(solution2(temp1, temp2))