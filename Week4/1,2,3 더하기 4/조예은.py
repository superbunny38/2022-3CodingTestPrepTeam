import sys


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    DP = [0] * 10000
    DP[0] = [1, 0, 0]
    DP[1] = [1, 1, 0]
    DP[2] = [2, 0, 1]
    testcase = list(int(sys.stdin.readline()) for _ in range(n))
    
    for i in range(3, max(testcase)):
        DP[i] = [sum(DP[i-1]), sum(DP[i-2][1:]), DP[i-3][2]]
    
    for num in testcase:
        print(sum(DP[num-1]))