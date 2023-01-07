from collections import deque
def solution(maps):
    def bfs(y, x):
        q = deque()
        q.append((y,x))
        maps[y][x] = 2
        while q:
            y,x = q.popleft()
            for dx,dy in d:
                Y, X = y + dy, x + dx
                if 0<=Y<len(maps) and 0<=X<len(maps[0]) and maps[Y][X] == 1:
                    maps[Y][X] = maps[y][x] + 1
                    q.append((Y,X))
        
    d = [(1,0),(-1,0),(0,1),(0,-1)]
    bfs(0,0)

    if maps[-1][-1] == 1:
        return -1
    return maps[-1][-1] - 1