class Personality:
    def __init__(self) -> None:
        self.score = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    def __call__(self):
        indexes = ['RT', 'CF', 'JM', 'AN']
        ret = ''
        for index in indexes:
            if self.score[index[0]] >= self.score[index[1]]:
                ret += index[0]
            else:
                ret += index[1]
        return ret

    def survey(self, type, choice):
        select = type[choice // 4]
        score = abs(4 - choice)
        self.score[select] += score

        
def solution(survey, choices):
    personality = Personality()
    for i in range(len(survey)):
        type = survey[i]
        choice = choices[i]
        personality.survey(type, choice)
    answer = personality()
    return answer
    
    
if __name__ == '__main__':
    survey = ["TR", "RT", "TR"]
    choices = [7, 1, 3]
    print(solution(survey, choices))