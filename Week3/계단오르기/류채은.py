
def main(scores):
    n = len(scores)
    max_scores_list = [[] for _ in range(n)]

    if n <=2:
        return sum(scores)
    else:
        max_scores_list[0] = [scores[0]]
        max_scores_list[1] = [scores[0]+scores[1],scores[1]]
        #print(max_scores_list)
        idx = 2
        while idx<len(scores):
            step1 = max_scores_list[idx-1][1]+scores[idx]
            step2 = max(max_scores_list[idx-2])+scores[idx]
            max_scores_list[idx] = [step1,step2]
            idx+=1
                
    #print(max_scores_list)
    return max(max_scores_list[n-1])


scores = []
n = int(input())
for _ in range(n):
    s = int(input())
    scores.append(s)
    
print(main(scores))
