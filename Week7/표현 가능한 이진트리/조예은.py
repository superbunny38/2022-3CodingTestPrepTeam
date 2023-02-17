import math


def check(number):
    flag = 1
    length = int(math.log(number, 2)) + 1
    width = 2**((int(math.log(length, 2)))+1) - 1
    binum = format(number, 'b').zfill(width)
    root = (width + 1) // 2
    queue = [(root, width, int(binum[root-1]))]
    
    while queue:
        root, width, check = queue.pop(0)
        if root <= 1:
            break
        d = width // 4 + 1
        left = root - d
        right = root + d
        width = width // 2
        
        lcheck = int(binum[left-1])
        rcheck = int(binum[right-1])
        
        if check == 0:
            if (lcheck == 1) or (rcheck == 1):
                flag = 0
                break
            else:
                queue.append((left, width, check))
                queue.append((right, width, check))
        else:
            queue.append((left, width, lcheck))
            queue.append((right, width, rcheck))
    
    return flag


def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(check(number))
    print(answer)
    return answer

numbers = [63, 111, 95]	
solution(numbers)