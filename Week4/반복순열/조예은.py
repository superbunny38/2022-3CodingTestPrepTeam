import sys


A, P = map(int, sys.stdin.readline().split())  # 수열의 첫 번째 숫자와 지수를 입력
D = dict()  # 수열의 숫자: 이전 수열의 길이


# 자릿수 P제곱의 합
def calculate(n):
    ret = 0
    for c in str(n):
        ret += int(c)**P
    return ret


# DFS 탐색: 현재 숫자, 수열의 길이
def dfs(n, l):
    if n in D:  # 방문한 숫자면
        return D[n]  # 그 숫자 이전 수열의 길이를 반환
    next = calculate(n)  # 다음 숫자
    D[n] = l
    ret = dfs(next, l + 1)
    return ret


if __name__ == '__main__':
    answer = dfs(A, 0)
    print(answer)