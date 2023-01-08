from collections import deque

def main() -> None:
    r, c, trashNumber = map(int, input().split())
    board = [[0] * c for _ in range(r)]
    for _ in range(trashNumber):
        y, x = map(int, input().split())
        board[y - 1][x - 1] = 1

    res = solve(r, c, board)
    print(res)
    return

def solve(r, c, board) -> int:
    res = 0
    visited = [[False] * c for _ in range(r)]
    
    for y in range(r):
        for x in range(c):
            if visited[y][x] or board[y][x] == 0:
                continue
            trashCnt = bfs(x, y, r, c, board, visited)
            res = max(res, trashCnt)
                 
    return res

def bfs(x, y, r, c, board, visited) -> int:
    dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    trashCnt = 1
    dq = deque([(x, y)])
    visited[y][x] = True
    while dq:
        x, y = dq.popleft()
        for dx, dy in dir:
            tx ,ty = x + dx, y + dy
            if not isRange(tx, ty, r, c) or visited[ty][tx] or board[ty][tx] == 0:
                continue
            dq.append((tx, ty))
            visited[ty][tx] = True
            trashCnt += 1
    
    return trashCnt

def isRange(x, y, r, c):
    return 0 <= x < c and 0 <= y < r

main()