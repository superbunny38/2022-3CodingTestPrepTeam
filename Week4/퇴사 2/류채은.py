#15486
#류채은
#풀이 참조

N = int(input())
T = []
P = []
memoization = [0 for _ in range(N+1)]

for _ in range(N):
    ti, pi = map(int, input().split())
    T.append(ti)
    P.append(pi)

k = 0
for i in range(N):
    k = max(k, memoization[i])
    if i + T[i]>N:
        continue
    memoization[i+T[i]] = max(k+P[i],memoization[i+T[i]])

print(max(memoization))


