#4963
#섬의 개수
#류채은
#21mins

def count_islands(graph,w,h):
    visited = [[0 for p in range(w)] for _ in range(h)]
    dx = [-1,1,0]
    dy = [-1,1,0]
    stack = []
    num_island = 0
    
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and visited[i][j] == 0:#island not visited
                stack = [(i,j)]
                while stack:
                    cur_y, cur_x = stack.pop(-1)
                    visited[cur_y][cur_x] = 1
                    for move_y in dy:
                        for move_x in dx:
                            if move_y == 0 and move_x == 0:
                                continue
                            if cur_y+move_y < h and cur_y+move_y >= 0 and cur_x+move_x>=0 and cur_x+move_x < w and graph[cur_y+move_y][cur_x+move_x] == 1 and visited[cur_y+move_y][cur_x+move_x] == 0:
                                stack.append((cur_y+move_y,cur_x+move_x))
                num_island +=1
    return num_island

#graphs = []
answers = []
#get inputs
while True:
    graph = []
    w,h = map(int, input().split())
    if w == 0 and h == 0:
        break
    for _ in range(h):
        tmp_row = list(input().split())
        #print("tmp_row:",tmp_row)
        tmp_row = [int(x) for x in tmp_row]
        graph.append(tmp_row)
        
    #graphs.append(graph)
    ##calculate number of islands
    answer = count_islands(graph, w,h)
    #print(answer)
    answers.append(answer)

for value in answers:
    print(value)
    
