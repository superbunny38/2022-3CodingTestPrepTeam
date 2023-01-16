import copy

def age(graph):
    orig_graph = copy.deepcopy(graph)
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    for i in range(1,len(graph)-1):
        for j in range(1,len(graph[0])-1):
            if orig_graph[i][j] != 0:
                n_age = 0
                for x,y in zip(dx,dy):
                    if orig_graph[i+y][j+x] == 0:
                        n_age +=1
                graph[i][j] = max(0,graph[i][j]-n_age)
       
        
        
                
def get_fragments(graph):
    visited = [[0 for _ in range(len(graph[0]))] for tmp in range(len(graph))]
    #queue = []
    n_count = 0
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    for i in range(1,len(graph)-1):
        for j in range(1,len(graph[0])-1):
            if graph[i][j] != 0 and visited[i][j] == 0:
                queue = [[i,j]]
                visited[i][j] = 1
                while queue:
                    popped = queue.pop(0)
                    y,x = popped[0],popped[1]
                    for move_x,move_y in zip(dx,dy):
                        if visited[y+move_y][x+move_x] == 0 and graph[y+move_y][x+move_x] != 0:
                            queue.append([y+move_y,x+move_x])
                            visited[move_y+y][move_x+x] = 1
                n_count+=1
    return n_count            
                
    
graph=[]

R,C = map(int, input().split())
for _ in range(R):
    tmp_row = list(input().split())
    tmp_row = [int(x) for x in tmp_row]
    graph.append(tmp_row)

n_age = 0
non_zero_pos = []
while True:
    age(graph)
    n_count = get_fragments(graph)
    n_age+=1
    #print(f"{n_age} year later... 덩어리:{n_count}")
    
    if n_count > 1:
        print(n_age)
        break
