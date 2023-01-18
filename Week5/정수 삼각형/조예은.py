import sys


input = sys.stdin.readline

n = int(input())
pyramid = list()


for i in range(n):
    pyramid.append(list(map(int, input().split())))


def solution():
    maximum = [[0] * i for i in range(1, n + 1)]
    for i in range(n):
        k = n - i - 1
        for j in range(k+1):
            if k == n - 1:
                maximum[k][j] = pyramid[k][j]
            else:
                maximum[k][j] = max(maximum[k+1][j], maximum[k+1][j+1]) + pyramid[k][j]
    print(maximum[0][0])

solution()