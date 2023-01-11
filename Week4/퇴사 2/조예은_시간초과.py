import sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    T = [0] * N
    P = [0] * N
    profit = [0] * (N+1)
    
    for i in range(N):
        t, p = map(int, sys.stdin.readline().split())
        T[i] = t
        P[i] = p
    
    maximum = 0
    for i in range(N):
        if i + T[i] > N:
            continue
        for j in range(i + T[i], N+1):
            profit[j] = max(profit[j], profit[i] + P[i])
        if maximum < profit[i] + P[i]:
            maximum = profit[i] + P[i]
            
    print(maximum)