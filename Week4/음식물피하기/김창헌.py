from collections import deque

N, M, K = map(int, input().split())
road = [[0] * (M + 1) for _ in range(N + 1)]
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for i in range(K):
    x, y = map(int, input().split())
    road[x][y] = '#'


def bfs(x, y):
    road[x][y] = 1
    q = deque()
    q.append((x, y))
    result = 1
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            X, Y = x + dx, y + dy
            if (0 < X <= N) and (0 < Y <= M) and road[X][Y] == '#':
                q.append((X, Y))
                road[X][Y] = road[x][y] + 1
                result += 1
    return result

answer = 0
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if road[i][j] == '#':
            ans = bfs(i, j)
            answer = max(answer, ans)
print(answer)
