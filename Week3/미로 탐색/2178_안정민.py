from collections import deque

def main():
    n, m = map(int, input().split())
    maze = [input() for _ in range(n)] 
    
    result = solve(n, m, maze)
    print(result)
    
def solve(n, m, maze) -> int:
    
    dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    dist = [[0 for _ in range(m)] for _ in range(n)]
    dist[0][0] = 1
    
    dq = deque([(0, 0)])
    while dq:
        x, y = dq.popleft()
        if [x, y] == [m - 1, n - 1]:
            break
        
        for dx, dy in dir:
            tx, ty = x + dx, y + dy
            if not isRange(tx, ty, n, m) or maze[ty][tx] == "0" or dist[ty][tx] != 0:
                continue
            
            dq.append((tx, ty))
            dist[ty][tx] = dist[y][x] + 1
    
    return dist[n - 1][m - 1]

def isRange(x, y, n, m):
    return 0 <= x < m and 0 <= y < n

main()