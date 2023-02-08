import copy
N = int(input())#N houses
costs = []
for _ in range(N):
    tmp_cost = input().split()
    tmp_cost = [int(x) for x in tmp_cost]
    costs.append(tmp_cost)

memoization = copy.deepcopy(costs)
print(memoization)
for house_idx in range(1,N):
    print("house_idx:",house_idx)
    prev_idx = house_idx-1
    #R
    memoization[house_idx][0] = min(memoization[prev_idx][1],memoization[prev_idx][2])+costs[house_idx][0]
    #G
    memoization[house_idx][1] = min(memoization[prev_idx][0],memoization[prev_idx][2])+costs[house_idx][1]
    #B
    memoization[house_idx][2] = min(memoization[prev_idx][0],memoization[prev_idx][1])+costs[house_idx][2]
    
print(min(memoization[-1]))
