import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))


if __name__ == '__main__':
    DP = [1] * N
    
    for i in range(1, len(A)):
        for j in range(0, i):
            if (A[i] < A[j]) & (DP[i] < DP[j] + 1):
                DP[i] = DP[j] + 1  # max를 계속 저장
    
    print(max(DP))