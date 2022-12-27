def dfs(y, x, cnt):
    c = maps[y][x]
    maps[y][x] = 1
    for dy, dx in d:
        Y, X = y+dy, x+dx
        if (0 <= Y < M) and (0 <= X < N) and maps[Y][X] == c:
            cnt = dfs(Y, X, cnt+1)
    return cnt

N, M = map(int, input().split())
maps = [list(input()) for _ in range(M)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
w = b = 0
for i in range(M):
    for j in range(N):
        if maps[i][j] == 'W':
            w += dfs(i, j, 1)**2
        elif maps[i][j] == 'B':
            b += dfs(i, j, 1)**2
print(w, b)