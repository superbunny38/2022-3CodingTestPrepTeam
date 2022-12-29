#1303
#류채은
#전쟁-전투


def dfs_get_power(graph,visited,i,j):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    stack = [(i,j)]
    m,n = len(graph), len(graph[0])
    label = graph[i][j]
    tmp = 0
    
    while stack:
        cur = stack.pop(-1)
        cur_y, cur_x = cur[0], cur[1]
        if visited[cur_y][cur_x] == 0:
            visited[cur_y][cur_x] = 1
            tmp +=1
            for move_x, move_y in zip(dx,dy):
                if cur_y+move_y >=0 and cur_y+move_y < m and cur_x+move_x >=0 and cur_x+move_x < n:
                    if graph[cur_y+move_y][cur_x+move_x] == label:
                        stack.append((cur_y+move_y,cur_x+move_x))
    return tmp**2
                        
def bfs_get_power(graph,visited,i,j):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue = [(i,j)]
    m,n = len(graph), len(graph[0])
    label = graph[i][j]
    tmp = 0
    
    while queue:
        cur = queue.pop(0)
        cur_y, cur_x = cur[0], cur[1]
        if visited[cur_y][cur_x] == 0:
            visited[cur_y][cur_x] = 1
            tmp +=1
            for move_x, move_y in zip(dx,dy):
                if cur_y+move_y >=0 and cur_y+move_y < m and cur_x+move_x >=0 and cur_x+move_x < n:
                    if graph[cur_y+move_y][cur_x+move_x] == label:
                        queue.append((cur_y+move_y,cur_x+move_x))
    return tmp**2

graph= []
N,M = map(int, input().split())#M이 세로, N이 가로

for _ in range(M):
    tmp_row = list(input())[:N]
    graph.append(tmp_row)

visited = [[0 for _ in range(N)] for r in range(M)]

power = {'W':0, 'B':0}

for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            label = graph[i][j]
            #print(f"on: ({i},{j})")
            #tmp_power = dfs_get_power(graph,visited,i,j)
            tmp_power = bfs_get_power(graph,visited,i,j)
            #print(tmp_power)
            power[label] += tmp_power
            
print(list(power.values())[0],list(power.values())[1])
