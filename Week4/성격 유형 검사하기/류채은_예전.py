def solution(survey, choices):
    score_dict = [{'R':0,'T':0},{'C':0, 'F':0},{'J':0, 'M':0},{'A':0, 'N':0}]
    
    for s,choice in zip(survey,choices):
        disagree, agree = s[0],s[1]
        if choice == 4:
            continue
        else:
            if choice < 4:#disagree
                if choice == 1:
                    mark = 3
                elif choice == 2:
                    mark = 2
                elif choice == 3:
                    mark = 1
                for idx,d in enumerate(score_dict):
                    if disagree in d.keys():
                        score_dict[idx][disagree] +=mark
            else:#choice > 4agree
                if choice == 5:
                    mark = 1
                elif choice == 6:
                    mark = 2
                elif choice == 7:
                    mark = 3
                else:
                    print("error")
                for idx,d in enumerate(score_dict):
                    if agree in d.keys():
                        score_dict[idx][agree] +=mark
    answer = ''
    for s in score_dict:
        if s[list(s)[0]] == s[list(s)[1]]:
            answer += min(list(s)[0], list(s)[1])
        else:
            answer += max(s, key=s.get)
    return answer
