import copy

def solution(n, info):#n: 화살의 개수 info: 어피치가 맞힌 과녁 점수의 개수(10점 개수, 9점 개수,...,1점 맞힌 개수,0점 개수)
    print("appeach:",info)
    possible = []
    for idx in range(len(info)):
        if idx == 0:
            lion_info = [0 for _ in range(len(info))]
            score = 10-idx
            n_appeach_shot = info[idx]#어피치가 쏜 횟수
            #lion_info[0] = 0#지거나
            possible.append([0]+lion_info[1:])
            lion_info[0] = n_appeach_shot +1#이김
            possible.append(lion_info)
        elif idx == 10:
            new = []
            while possible:
                possible_answer = possible.pop(-1)
                if sum(possible_answer) == n:
                    new.append(possible_answer)
            possible = new
        else:
            new = []
            print("idx:",idx)
            print(possible)
            while possible:
                possible_answer=possible.pop(-1)
                if sum(possible_answer) > n:
                    continue
                n_appeach_shot = info[idx]
                possible_answer1 = copy.deepcopy(possible_answer)
                possible_answer1[idx] = 0
                new.append(possible_answer1)
                if n-sum(possible_answer)>=n_appeach_shot+1:
                    possible_answer[idx] = n_appeach_shot+1
                    new.append(possible_answer)
            possible = new
        
    print("final:",possible)
    answers = []
    for is_answer in possible:
        score = 10
        appeach_score = 0
        lion_score = 0
        for lion,appeach in zip(is_answer,info):
            if lion>appeach:
                lion_score += score
            else:
                appeach_score += score
            score -=1
        if appeach_score<lion_score:
            print("won:",is_answer)
            answers.append("".join(is_answer))
    print(answers)
    if len(answers)>0:
        real_answer = sorted(answers)[0]
        real_answer = list(real_answer)
        real_answer = [int(x) for x in real_answer]
    else:
        answer = [-1]#비기거나 무조건 지는 경우
        return answer

n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]
print(solution(n,info))
