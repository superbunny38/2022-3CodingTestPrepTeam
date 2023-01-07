import sys

input = sys.stdin.readline
n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1  # 초기 값

# 반복문을 통해 갈 수 있는 그래프의 좌표를 탐색
for i in range(n):
    for j in range(n):
        # 현재 탐색하는 좌표가 오른쪽 맨 끝 점이면 반복을 멈춘다.
        if i == n - 1 and j == n - 1:
            print(dp[i][j])
            break

        # 오른쪽으로 이동
        if j + maps[i][j] < n:
            dp[i][j + maps[i][j]] += dp[i][j]

        # 아래로 이동
        if i + maps[i][j] < n:
            dp[i + maps[i][j]][j] += dp[i][j]
