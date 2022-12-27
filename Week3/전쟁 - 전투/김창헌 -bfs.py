from collections import deque

def bfs(y, x):
    q = deque()
    q.append((y, x))
    c = graph[y][x]
    graph[y][x] = 1
    cnt = 0
    while q:
        y, x = q.popleft()
        cnt += 1
        for dy, dx in d:
            Y, X = y+dy, x+dx
            if (0 <= Y < M) and (0 <= X < N) and graph[Y][X] == c:
                q.append((Y, X))
                graph[Y][X] = 1
    return cnt

N, M = map(int, input().split())
graph = [list(input()) for _ in range(M)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
w = b = 0
for i in range(M):
    for j in range(N):
        if graph[i][j] == 'W':
            w += bfs(i, j)**2
        elif graph[i][j] == 'B':
            b += bfs(i, j)**2
print(w, b)