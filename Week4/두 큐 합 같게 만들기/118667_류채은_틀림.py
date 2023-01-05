def solution(queue1, queue2):
    answer = -1
    same_sum = (sum(queue1)+sum(queue2))/2
    
    if (sum(queue1)+sum(queue2))%2 != 0:
        return answer
    def pop(queue):
        popped = queue.pop(0)
        return popped
    def insert(queue, item):
        queue.append(item)
    count = 0
    while True:
        sum1,sum2 = sum(queue1),sum(queue2)
        
        if sum1 == sum2:
            answer = count
            break
        while sum1 < sum2:
            popped = pop(queue2)
            insert(queue1, popped)
            count +=1
            sum1,sum2 = sum(queue1),sum(queue2)
        while sum2 < sum1:
            popped = pop(queue1)
            insert(queue2, popped)
            count+=1
            sum1,sum2 = sum(queue1),sum(queue2)
        if count >= len(queue1)+len(queue2):
            break
        
    return answer
