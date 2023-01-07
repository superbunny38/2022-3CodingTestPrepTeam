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