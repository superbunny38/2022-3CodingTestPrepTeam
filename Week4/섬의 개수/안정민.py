from collections import deque

def main() -> None:
    while True:
        c, r = map(int, input().split())
        if [c, r] == [0, 0]:
            return
        land = [list(map(int, input().split())) for _ in range(r)]
        
        landCnt = 0
        
        visited = [[False] * c for _ in range(r)]
        for y in range(r):
            for x in range(c):
                if visited[y][x] or land[y][x] == 0:
                    continue
                landCnt += 1
                bfs(x, y, land, visited)
        
        print(landCnt)

def bfs(x, y, land, visited) -> None:
    dir = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
    r, c = len(land), len(land[0])
    
    dq = deque([(x, y)])
    visited[y][x] = True
    while dq:
        x, y = dq.popleft()
        for dx, dy in dir:
            tx, ty = x + dx, y + dy
            if not isRange(tx, ty, r, c) or visited[ty][tx] or land[ty][tx] == 0:
                continue
            dq.append((tx, ty))
            visited[ty][tx] = True
            
    return

def isRange(x, y, r, c) -> bool:
    return 0 <= x < c and 0 <= y < r

main()