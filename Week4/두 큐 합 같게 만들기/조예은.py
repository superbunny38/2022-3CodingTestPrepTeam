# 두 수의 합의 절반이 넘는 숫자가 있으면 return -1
from collections import deque


def solution(queue1, queue2):
    now = sum(queue1)
    target = now + sum(queue2)
    
    if target % 2 == 1:  # 홀수면 같게 만들 수 없다.
        return -1
    else:
        target //= 2
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    answer = 0
    
    # 각 queue의 최대 길이는 30만. 60만번 하면 두 queue가 뒤바뀌는 경우가 적어도 한번 존재한다.
    for _ in range(600000):
        if now == target:
            return answer
        
        # queue1 -> queue2
        if now > target:
            n = queue1.popleft()
            queue2.append(n)
            now -= n
            answer += 1
        
        # queue2 -> queue1
        if now < target:
            n = queue2.popleft()
            queue1.append(n)
            now += n
            answer += 1

        if n > target:  # 절반보다 큰 수가 있으면 절대 같게 만들 수 없다.
            return -1
    return -1


if __name__ == '__main__':
    queue1 = [1, 2, 1, 2]
    queue2 = [1, 10, 1, 2]
    
    print(solution(queue1, queue2))