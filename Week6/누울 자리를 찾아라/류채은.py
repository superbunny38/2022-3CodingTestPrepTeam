import copy

def check(graph,N):
    visited_garo = [[0]*N for _ in range(N)]
    visited_sero = [[0]*N for _ in range(N)]
    n_garo,n_sero = 0,0
    
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 'X':
                continue
            
            if j+1<N and visited_garo[i][j] == 0 and visited_garo[i][j+1] == 0 and graph[i][j+1] == '.':
                visited_garo[i][j] = 1
                visited_garo[i][j+1] = 1
                n_garo += 1
                move_x = 2
                while move_x+j<N:
                    if graph[i][j+move_x] == '.' and visited_garo[i][j+move_x] == 0:
                        visited_garo[i][j+move_x] = 1
                        move_x+=1
                    else:
                        break
                      
            if i+1<N and visited_sero[i][j] == 0 and visited_sero[i+1][j] == 0 and graph[i+1][j] == '.':
                visited_sero[i][j]=1
                visited_sero[i+1][j]=1
                n_sero += 1
                move_y = 2
                while move_y+i<N:
                    if graph[move_y+i][j] == '.' and visited_sero[move_y+i][j] == 0:
                        visited_sero[move_y+i][j] =1
                        move_y+=1
                    else:
                        break                
                
    return n_garo,n_sero
                

N = int(input())
graph = []
for _ in range(N):
    tmp_row = input()[:N+1]
    graph.append(tmp_row)

n_garo,n_sero = check(graph,N)

print(n_garo,n_sero)
