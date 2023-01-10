#1743
#류채은
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
import copy
N,M,K = map(int, input().split())
graph = [[0 for _ in range(M)] for r in range(N)]
visited = [[0 for w in range(M)] for q in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
trash = []

for _ in range(K):
    y_,x_ = map(int, input().split())
    graph[y_-1][x_-1] = 1
    trash.append([y_-1,x_-1])
    
max_cost = 0

#bfs
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and graph[i][j] == 1:
            cost = 1
            queue = []
            queue.append([i,j])
            visited[i][j] = 1
            while queue:
                popped = queue.pop(0)
                cur_y, cur_x = popped[0],popped[1]
                print(f"visiting: ({cur_y},{cur_x})")
                #visited[cur_y][cur_x] = 1
                for move_y, move_x in zip(dy,dx):
                    if 0<=move_y+cur_y<N and 0<=move_x+cur_x<M and visited[move_y+cur_y][move_x+cur_x] == 0 and graph[move_y+cur_y][move_x+cur_x] == 1:
                        queue.append([cur_y+move_y,cur_x+move_x])
                        visited[move_y+cur_y][move_x+cur_x] = 1
                        cost+=1
                    #print("cost:",cost)
            if max_cost <cost:
                max_cost = cost
print(max_cost)
                            
                    
                    
                    
