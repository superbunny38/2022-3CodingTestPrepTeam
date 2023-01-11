import sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    DP = [0] * (N)
    for i in range(N):
        n = int(sys.stdin.readline())
        if i == 0:
            DP[i] = (n, 0)
        elif i == 1:
            DP[i] = (n + DP[i-1][0], n)
        else:
            DP[i] = (DP[i-1][1] + n, max(DP[i-2]) + n)
    print(max(DP[N-1]))