#아기 상어
#16236

class Shark:
    def __init__(self):
        self.size = 2
        self.ate = 2
        
graph = []
N = int(input())
visited = [[0]*N for _ in range(N)]
fishes = []
for _ in range(N):
    tmp_row = input().split()
    tmp_row = [int(x) for x in tmp_row]
    if 9 in tmp_row:
        shark_x = tmp_row.index(9)
        shark_y = _
    graph.append(tmp_row)

for i in range(N):
    for j in range(N):
        if graph[i][j] != 0 and graph[i][j]!=9:
            fishes.append(graph[i][j])
fishes= sorted(fishes)
print("fishes:",fishes)

dx = [0,-1,1,0]
dy = [-1,0,0,1]
stack = [[shark_y,shark_x]]
graph[shark_y][shark_x] = 0
shark = Shark()
move = 0

while stack:
    if len(fishes) == 0:
        break
    elif fishes[0] > shark.size:
        break
    cur_pos = stack.pop(0)
    cur_y,cur_x = cur_pos[0],cur_pos[1]    
    fish = graph[cur_y][cur_x]
    
    if fish != 0:
        #print("fishes:",fishes,"fish:",fish)
        
        if shark.size == fish:
            move = move+visited[cur_y][cur_x]
            for v in visited:
                print(v)
            print(f"[{cur_y},{cur_x}] ate fish:",fish, "shark size:",shark.size, "moved:",move)
            
        elif shark.size > fish:
            fishes.remove(fish)
            graph[cur_y][cur_x] = 0
            move = move+visited[cur_y][cur_x]
            shark.ate -= 1
            if shark.ate == 0:
                shark.size +=1
                shark.ate = shark.size
            for v in visited:
                print(v)
            visited = [[0]*N for _ in range(N)]
            stack = [[cur_y,cur_x]]
            print(f"[{cur_y},{cur_x}]ate fish:",fish, "shark size:",shark.size, "moved:",move)
            
    for move_y, move_x in zip(dy,dx):
        if 0<=cur_y+move_y<N and 0<=cur_x+move_x<N and graph[cur_y+move_y][cur_x+move_x] <= shark.size and visited[cur_y+move_y][cur_x+move_x] == 0:
            visited[cur_y+move_y][cur_x+move_x] = visited[cur_y][cur_x]+1
            stack.append([cur_y+move_y,cur_x+move_x])
print(move)  
