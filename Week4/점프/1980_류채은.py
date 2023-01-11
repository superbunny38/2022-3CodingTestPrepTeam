
N = int(input())
graph = []

for _ in range(N):
    row = input().split()
    row = [int(x) for x in row]
    graph.append(row)

stack = [(0,0)]
count = 0

while True:
    if len(stack) == 0:
        break
    cur = stack.pop(0)
    cur_y, cur_x = cur[0],cur[1]
    n_move = graph[cur_y][cur_x]
    if cur_y == N-1 and cur_x == N-1:
        count +=1
        continue
    #move right
    if cur_x+n_move <N:
        stack.append((cur_y,cur_x+n_move))
    #move down
    if cur_y+n_move<N:
        stack.append((cur_y+n_move,cur_x))
print(count)
    
