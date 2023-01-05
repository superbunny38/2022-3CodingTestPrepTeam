import sys
from collections import deque


def bfs(y, x, land_map):
    q = deque()
    q.append((y, x))
    land_map[y][x] = 0
    while q:
        y, x = q.popleft()
        for dx, dy in d:
            X, Y = x + dx, y + dy
            if 0 <= X < w and 0 <= Y < h and land_map[Y][X] == 1:
                land_map[Y][X] = 0
                q.append((Y, X))

input = sys.stdin.readline
d = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1),(-1,1),(1,-1),(-1,-1)]
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    land_map = [list(map(int,input().split())) for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if land_map[i][j] == 1:
                ans += 1
                bfs(i, j, land_map)
    print(ans)
