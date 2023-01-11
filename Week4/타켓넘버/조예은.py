from collections import deque

def bfs(numbers, target):
    queue = deque()
    queue.append([0, 0])
    ret = 0
    while queue:
        i, s = queue.popleft()
        if i == len(numbers):
            if s == target:
                ret += 1
            continue
        queue.append([i+1, s + numbers[i]])
        queue.append([i+1, s - numbers[i]])
    return ret


def solution(numbers, target):
    answer = bfs(numbers, target)
    return answer


if __name__ == '__main__':
    numbers = [4, 1, 2, 1]
    target = 4
    print(solution(numbers, target))