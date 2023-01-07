def solution(survey, choices) -> str:
    answer = ''
    score = { "R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0 }
    for suv, value in zip(survey, choices):
        a, b = list(suv)
        if value < 4:
            score[a] += 4 - value
        elif value > 4:
            score[b] += value - 4
    
    scoreList = list(score.items())
    for i in range(0, 8, 2):
        a, b = scoreList[i], scoreList[i + 1]
        answer += b[0] if a[1] < b[1] else a[0]
        
    return answer