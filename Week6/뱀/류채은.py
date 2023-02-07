import copy
def change_direction(move_y,move_x,change_dir):
    if move_y == 0 and move_x == 1:#was going right
        if change_dir == 'L':#왼쪽으로 90도 회전
            #move_y,move_x =-1,0#move up
            return -1,0
        elif change_dir == 'D':#오른쪽으로 90도 회전
            #move_y,move_x = 1,0#move down
            return 1,0
    elif move_y == 0 and move_x== -1:#was going left
        if change_dir == 'L':#왼쪽으로 90도 회전
            return 1,0#move down
        elif change_dir == 'D':
            return -1,0
    elif move_y == -1 and move_x == 0:#was moving up
        if change_dir == 'L':#왼쪽으로 90도 회전
            return 0,-1#move left
        elif change_dir == 'D':
            return 0,1
    elif move_y == 1 and move_x == 0:#was moving down
        if change_dir == 'L':
            return 0,1
        elif change_dir == 'D':
            return 0,-1
            

N = int(input())
K = int(input())
graph = [[0]*(N+2) for _ in range(N+2)]#벽 때문에 zero padding

for _ in range(K):
    tmp_y,tmp_x = map(int,input().split())
    graph[tmp_y][tmp_x] = 'a'

L = int(input())
directions = []

for _ in range(L):
    tmp = input().split()
    tmp_sec, tmp_dir = int(tmp[0]),tmp[1]
    directions.append([tmp_sec,tmp_dir])

sec = 0#second elapsed
popped = directions.pop(0)
change_sec,change_dir = popped[0],popped[1]
move_y,move_x = 0,1#move right first
size = 1
cur_y,cur_x = 1,1
snake_pos = [[1,1]]

while True:
    if sec == change_sec:
        move_y,move_x = change_direction(move_y,move_x,change_dir)
        if directions:
            popped = directions.pop(0)
            change_sec,change_dir = popped[0],popped[1]
        
    cur_y,cur_x = cur_y+move_y,cur_x+move_x
    if cur_y == 0 or cur_x == 0 or cur_y == N+1 or cur_x == N+1:
        sec +=1
        break
    if graph[cur_y][cur_x] =='s':#met snake
        sec +=1
        break
    if graph[cur_y][cur_x] == 'a':#apple
        snake_pos.append([cur_y,cur_x])
    else:
        #cut tail
        popped = snake_pos.pop(0)
        tail_y,tail_x = popped[0],popped[1]
        graph[tail_y][tail_x] = 0
        snake_pos.append([cur_y,cur_x])
    graph[cur_y][cur_x] = 's'
        
    sec +=1
    #print("second elapsed:",sec)
    #print("graph:")
    #for g in graph:
    #    print(g)

print(sec)
