import copy

def solve(n,sizes):
    if n == 1:
        return sizes[-1]
    memoization = [0]+copy.deepcopy(sizes)
    #print(memoization)
    memoization[1] = sizes[0]+sizes[1]
    memoization[2] = sizes[1]+sizes[2]
    for i in range(3,n+1):
        option1 = memoization[i-2]+sizes[i]
        option2 = memoization[i-3]+sizes[i-1]+sizes[i]
        option3 = memoization[i-1]#지금 잔 안 마심
        memoization[i] = max(option1,option2,option3)
    #print(memoization)
    return memoization[n]

    
n = int(input())
sizes = [0,]
for _ in range(n):
    tmp_size = int(input())
    sizes.append(tmp_size)

print(solve(n,sizes))
