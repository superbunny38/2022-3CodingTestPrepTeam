from collections import deque

def bfs(y,x):
  queue = deque()
  queue.append((y,x))  
  while queue:
    y, x = queue.popleft()
    for dx, dy in d:
      X, Y = x+dx, y+dy
      if (0 <= X < M) and (0 <= Y < N) and maze[Y][X] == 1:
        queue.append((Y,X))
        maze[Y][X] = maze[y][x]+1
  return maze[N-1][M-1]
      
N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
d = [(1,0),(-1,0),(0,1),(0,-1)]
print(bfs(0,0))
