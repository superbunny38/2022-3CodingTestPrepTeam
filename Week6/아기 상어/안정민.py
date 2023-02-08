from collections import deque

def checkClosestFish(shark, board):
    sx, sy, sw = shark
    n = len(board)
    catched = []

    visited = [[0] * n for _ in range(n)]
    dq = deque([(sx, sy)])
    visited[sy][sx] = -1
    while dq:
        x, y = dq.popleft()
        for dx, dy in dir:
            tx, ty = x + dx, y + dy
            if not isRange(tx, ty, len(board)) or visited[ty][tx] != 0:
                continue
            fishWeight = board[ty][tx]
            if fishWeight > sw:
                continue
            elif fishWeight == sw or fishWeight == 0:
                dq.append((tx, ty))
                visited[ty][tx] = visited[y][x] + 1
            else:
                catched.append((tx, ty, visited[y][x] + 1))
        
    if len(catched) == 0:
        return -1
    
    res = sorted(catched, key = lambda x: (x[2], x[1], x[0]))
    return res[0]
            
def isRange(x, y, n):
    return 0 <= x < n and 0 <= y < n
        
dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
n = int(input())
shark = [0, 0, 0]
eatCnt = 0
board = []
for y in range(n):
    temp = list(map(int, input().split()))
    for x in range(n):
        curr = temp[x]
        if curr == 9:
            shark = [x, y, 2]
    board.append(temp)
board[shark[1]][shark[0]] = 0

time = 0
while True:
    res = checkClosestFish(shark, board)
    if res == -1:
        break
    sx, sy, sw = shark
    nx, ny, t = res
    board[ny][nx] = 0
    shark[0], shark[1] = nx, ny
    time += t + 1
    
    eatCnt += 1
    if eatCnt == sw:
        eatCnt = 0
        shark[2] += 1

print(time)    
 
