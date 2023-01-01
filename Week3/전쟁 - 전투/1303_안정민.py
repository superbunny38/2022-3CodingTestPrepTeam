from collections import deque

def main():
    n, m = map(int, input().split())
    field = [input() for _ in range(m)]
    white, blue = solve(n, m, field)
    
    print(white, blue)

def solve(n, m, field):
    def check(x, y):
        visited[y][x] = True
        dq.append((x, y))
    
    dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    totalScore = { "W": 0, "B": 0 }
    visited = [[False for _ in range(n)] for _ in range(m)]
 
    while 1:
        x, y = getNotCheckedPos(visited)
        if [x, y] == [-1, -1]:
            break
        
        team = field[y][x]
        teamCnt = 1

        dq = deque()
        check(x, y)
        while dq:
            x, y = dq.popleft()
            for dx, dy in dir:
                tx, ty = x + dx, y + dy
                if not isRange(tx, ty, n, m) or visited[ty][tx] or field[ty][tx] != team:
                    continue
                
                check(tx, ty)
                teamCnt += 1
        
        totalScore[team] += teamCnt**2
    
    return totalScore["W"], totalScore["B"]

def isRange(x, y, n, m):
    return 0 <= x < n and 0 <= y < m
        
def getNotCheckedPos(visited):
    n, m = len(visited[0]), len(visited)
    for y in range(m):
        for x in range(n):
            if not visited[y][x]:
                return x, y
    return -1, -1

main()