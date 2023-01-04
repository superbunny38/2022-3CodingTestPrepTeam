def solution(maps):
    answer = 0
    stack = [(0,0)]#y,x
    N, M = len(maps), len(maps[0])
    visited = [[0 for w in range(M)] for _ in range(N)]
    cost = [[0 for w in range(M)] for _ in range(N)]
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    cost[0][0] = 1
    '''
    for g in maps:
        print(g)
    '''
    while stack:
        cur = stack.pop(0)
        cur_y, cur_x = cur[0], cur[1]
        if visited[cur_y][cur_x] == 0:
            visited[cur_y][cur_x] = 1
            #print(f"at: ({cur_y},{cur_x})")
            if cur_y == N-1 and cur_x == M-1:
                #print("cost:\n")
                #for c in cost:
                #    print(c)
                return cost[cur_y][cur_x]
            for move_y, move_x in zip(dy,dx):
                if move_y+cur_y >=0 and move_y+cur_y<N and move_x+cur_x >=0 and move_x+cur_x <M and visited[move_y+cur_y][move_x+cur_x] == 0 and maps[move_y+cur_y][move_x+cur_x] == 1:
                    stack.append((move_y+cur_y, move_x+cur_x))
                    
                    cost[move_y+cur_y][move_x+cur_x] = cost[cur_y][cur_x] + 1
                    
    if cur_y == N-1 and cur_x == M-1:
        return cost[cur_y][cur_x]
    answer = -1
    return answer
