#1463_류채은

n = int(input())

memoization = [0 for _ in range(n+1)]
memoization[1] = 0

for idx in range(1,n):
    real_idx = idx+1
    memoization[real_idx] = memoization[real_idx-1]+1
    if real_idx%2 == 0:
        memoization[real_idx] = min(memoization[real_idx], memoization[real_idx//2]+1)
    if real_idx%3 == 0:
        memoization[real_idx] = min(memoization[real_idx], memoization[real_idx//3]+1)

print(memoization[n])
