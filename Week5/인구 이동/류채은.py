
def break_barrier(graph,cur_pos, L,R,visited):
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    N = len(graph)
    queue = [cur_pos]
    break_list = [cur_pos]
    summ = graph[cur_pos[0]][cur_pos[1]]
    while queue:
        popped = queue.pop(0)
        y,x = popped[0],popped[1]
        for move_y, move_x in zip(dy,dx):
            if 0<=y+move_y<N and 0<=x+move_x<N and visited[move_y+y][move_x+x] == 0 and L<=abs(graph[move_y+y][move_x+x]-graph[y][x]) <=R:
                visited[y+move_y][x+move_x] = 1
                queue.append([y+move_y,x+move_x])
                break_list.append([y+move_y,x+move_x])
                summ+= graph[y+move_y][x+move_x]

    if len(break_list) >1:
        n_fill = int(summ/len(break_list))
        for break_ in break_list:
            break_y,break_x= break_[0],break_[1]
            graph[break_y][break_x] = n_fill
        return True
    else:
        return False
                
                
    
    

def move_people(graph,L,R):
    N = len(graph)
    visited = [[0 for _ in range(N)] for tmp in range(N)]
    move = False
    for i in range(N):
        for j in range(N):
            if visited[i][j] ==0:
                visited[i][j] = 1
                cur_pos = [i,j]
                res = break_barrier(graph,cur_pos,L,R,visited)
                if res == True:
                    move = True
    return move
                

N,L,R = map(int,input().split())
graph = []#NxN

for _ in range(N):
    tmp_row = list(input().split())
    tmp_row = [int(x) for x in tmp_row]
    graph.append(tmp_row)

day = 0
while True:
    result = move_people(graph,L,R)
    
    if result == True:
        day+=1
        
    else:
        break
print(day)
        
