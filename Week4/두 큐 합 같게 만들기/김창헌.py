from collections import deque
def solution(queue1, queue2):
    t1, t2 = sum(queue1), sum(queue2)
    total = t1+t2
    answer = 0
    limit = 600000
    
    if total % 2 != 0:
        return -1
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    while True:
        if t1>t2:
            temp = queue1.popleft()
            queue2.append(temp)
            t1 -= temp
            t2 += temp
            answer +=1
        elif t1<t2:
            temp = queue2.popleft()
            queue1.append(temp)
            t2 -= temp
            t1 += temp
            answer +=1
        else:
            break
        if answer == limit:
            answer =  -1
            break
            
    return answer