import copy

def solution(n, info):#n: 화살의 개수 info: 어피치가 맞힌 과녁 점수의 개수(10점 개수, 9점 개수,...,1점 맞힌 개수,0점 개수)
    #print("appeach:",info)
    possible = []
    for idx in range(len(info)):
        if idx == 0:
            lion_info = [0 for _ in range(len(info))]
            score = 10-idx
            n_appeach_shot = info[idx]#어피치가 쏜 횟수
            #lion_info[0] = 0#지거나
            lion_info1 = copy.deepcopy(lion_info)
            lion_info1[0] = 0
            possible.append(lion_info1)
            lion_info[0] = n_appeach_shot +1#이김
            possible.append(lion_info)
        elif idx == 10:#마지막
            new = []
            while possible:
                possible_answer = possible.pop(-1)
                if sum(possible_answer) == n:
                    new.append(possible_answer)
                elif sum(possible_answer) < n:
                    n_left = n-sum(possible_answer)
                    possible_answer[-1] = n_left
                    new.append(possible_answer)
            possible = new            
            break
        else:
            new = []
            while possible:
                possible_answer=possible.pop(-1)
                if sum(possible_answer) > n:
                    continue
                n_appeach_shot = info[idx]
                possible_answer1 = copy.deepcopy(possible_answer)
                possible_answer1[idx] = 0
                new.append(possible_answer1)
                possible_answer[idx] = n_appeach_shot+1
                if sum(possible_answer) <=n:
                    new.append(possible_answer)
            possible = new
        
    #print("final:",possible)
    answers = {}
    for is_answer in possible:
        #print("lion:",is_answer)
        #print("appeach:",info)
        score = 10
        appeach_score = 0
        lion_score = 0
        assert sum(is_answer) == n
        for lion,appeach in zip(is_answer,info):
            #print("lion:",lion,"appeach:",appeach)
            if lion == 0 and appeach ==0:
                pass
            else:
                if lion > appeach:
                    lion_score += score
                    #print("lion: +",score)
                else:
                    appeach_score += score
                    #print("appeach: +",score)
            score -=1
        
        #print("appeach score:",appeach_score)
        #print("lion score:",lion_score)
        if appeach_score<lion_score:
            gap = lion_score - appeach_score
            if gap in answers:
                answers[gap].append(is_answer)
            else:
                answers[gap] = [is_answer]                
    #print(answers)
    if answers:
        max_key = sorted(list(answers.keys()),reverse = True)[0]
        candidates = answers[max_key]
        if len(candidates) == 1:
            return candidates[0]
        str_candidates = []
        for c in candidates:
            c = [str(x) for x in c]
            str_candidates.append("".join(c)[::-1])
        #print(str_candidates)
        #print("here:",real_answer)
        real_answer = sorted(str_candidates,reverse = True)[0][::-1]
        real_answer = [int(x) for x in real_answer]
        return real_answer
    else:
        answer = [-1]#비기거나 무조건 지는 경우
        return answer

n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]
print(solution(n,info))

n = 1
info = [1,0,0,0,0,0,0,0,0,0,0]
print(solution(n,info))

n = 9
info = [0,0,1,2,0,1,1,1,1,1,1]
print(solution(n,info))

n = 10
info = [0,0,0,0,0,0,0,0,3,4,3]
print(solution(n,info))

