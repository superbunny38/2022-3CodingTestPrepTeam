#43165
def solution(numbers, target):
    answer = 0
    for idx,n in enumerate(numbers):
        if idx == 0:
            cum = [-n,+n]
        else:

            new_ans = []
            #print("cum:",cum)
            #print("iterate for:",idx**2)
            for _ in range(2**idx):
                cumulative = cum.pop(-1)
                #print("popped:",cumulative)
                new_ans.append(cumulative+n)
                new_ans.append(cumulative-n)
                #print("apending:",cumulative+1)
                #print("apending:",cumulative-1)
            cum = new_ans
    #print(cum)
    for c in cum:
        if c == target:
            answer+=1
                
                
    return answer
numbers = [1,1,1,1,1]
target = 3
print(solution(numbers,target))
