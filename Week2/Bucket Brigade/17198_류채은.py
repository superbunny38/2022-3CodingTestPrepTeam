#Bucket Brigade
#17198
#류채은

def can_pass(graph,new_y,new_x):
    if graph[new_y][new_x] == 'R':
        return False
    if graph[new_y][new_x] == 'x':
        return False
    return True

visited = [[0]*10 for _ in range(10)]
graph = []
for i in range(10):
    sub_list = list(input())
    assert len(sub_list) == 10, print(len(sub_list))
    if 'B' in sub_list:
        b_x,b_y = sub_list.index('B'),i
    if 'R' in sub_list:
        r_x,r_y = sub_list.index('R'),i
    if 'L' in sub_list:
        l_x,l_y = sub_list.index('L'),i
    graph.append(sub_list)
'''

print(f"where 불: ({b_y},{b_x})")
print(f"where 바위: ({r_y},{r_x})")
print(f"where 강: ({l_y},{l_x})")'''

dx = [-1,0,1,0]
dy = [0,1,0,-1]

start = (l_y,l_x)
end = (b_y,b_x)

visited = [[0]*10 for _ in range(10)]

queue = [start]
visited[l_y][l_x] = 1

while queue:
    y,x = queue.pop(0)
    if y == b_y and x == b_x:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 10 and 0 <= ny < 10 and can_pass(graph,ny,nx) == True and visited[ny][nx] == 0:
            visited[ny][nx] = visited[y][x] + 1
            graph[ny][nx] = 'x'
            queue.append((ny,nx))
'''
for v in visited:
    print(v)

for g in graph:
    print(g)
'''
print(visited[b_y][b_x]-2)
