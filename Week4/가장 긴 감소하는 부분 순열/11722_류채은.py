#11722
#가장 긴 감소하는 부분 수열
#Memoization

N = int(input())
num_array = list(input().split())
num_array = [int(x) for x in num_array]
memoization = [1 for _ in range(N)]

for i in range(N):
    #print("i:",i)
    cur = num_array[i]
    max_ = 0
    for j in range(i):
        #print(f"{num_array[j]} {cur}")
        if num_array[j] > cur:
            #print("j:",j)
            if max_ < memoization[j]:
                max_ = memoization[j]
    #print("max_:",max_)
    if max_ != 0:
        memoization[i] = max_+1
    

print(max(memoization))
