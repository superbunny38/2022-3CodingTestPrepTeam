from collections import deque

def solution(maps):
    dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    r, c = len(maps), len(maps[0])
    
    visited = [[0] * c for _ in range(r)]
    dq = deque([(0, 0)])
    while dq:
        x, y = dq.popleft()
        for dx, dy in dir:
            tx, ty = x + dx, y + dy
            if not isRange(tx, ty, r, c) or visited[ty][tx] != 0 or maps[ty][tx] == 0:
                continue
            
            visited[ty][tx] = visited[y][x] + 1
            dq.append((tx, ty))
    
    res = visited[r - 1][c - 1]
    return res + 1 if res != 0 else -1

def isRange(x, y, r, c):
    return 0 <= x < c and 0 <= y < r