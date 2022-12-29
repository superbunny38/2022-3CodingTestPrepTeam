#2178
#미로탐색

graph = []
N,M = map(int, input().split())
for _ in range(N):
    tmp_row = list(input())
    tmp_row = [int(x) for x in tmp_row]
    graph.append(tmp_row)

queue = [(0,0)]
visited = [[0 for _ in range(M)] for r in range(N)]
cost = [[N*M for _ in range(M)] for r in range(N)]
cost[0][0] = 1
#bfs
while queue:
    cur = queue.pop(0)
    cur_y, cur_x = cur[0],cur[1]
    #print(f"currently on: ({cur_y},{cur_x})")
    if cur_y == N-1 and cur_x == M-1:
        break
    if visited[cur_y][cur_x] == 0:
        cur_cost = cost[cur_y][cur_x]
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        visited[cur_y][cur_x] = 1
        for move_x, move_y in zip(dx,dy):
            if move_x+cur_x >=0 and move_x+cur_x<M and move_y+cur_y>=0 and move_y+cur_y<N and graph[move_y+cur_y][move_x+cur_x] == 1 and visited[move_y+cur_y][move_x+cur_x] == 0:
                cost[move_y+cur_y][move_x+cur_x] = min(cost[move_y+cur_y][move_x+cur_x],cur_cost+1)
                queue.append((move_y+cur_y,move_x+cur_x))
'''
print("original graph:")
for g in graph:
    print(g)

print("visited:")
for v in visited:
    print(v)

print("cost:")
for c in cost:
    print(c)

  '''  
print(cost[N-1][M-1])
