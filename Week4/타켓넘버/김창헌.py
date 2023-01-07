def solution(numbers, target):
    answer = 0
    dp = [0]
    for i in numbers:
        temp = []
        for j in dp:
            temp.append(j+i)
            temp.append(j-i)
        dp = temp
    return dp.count(target)