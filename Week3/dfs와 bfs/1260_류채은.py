#1260
#DFS와 BFS

def dfs(graph, start_v):
    stack= [start_v]
    visited = []
    idx = 0
    print_list = []
    while stack:
        item = stack.pop(-1)
        if item not in visited:
            print_list.append(item)
            idx+=1
            visited.append(item)
            stack += sorted(graph[item])[::-1]

    for idx, item in enumerate(print_list):
        if idx == len(print_list)-1:
            print(item)
        else:
            print(item, end = " ")


def bfs(graph, start_v):
    queue = [start_v]
    visited = []
    print_list = []
    idx = 0
    while queue:
        item = queue.pop(0)
        if item not in visited:
            print_list.append(item)
           
            idx+=1
            visited.append(item)
            queue += sorted(graph[item])
    for idx, item in enumerate(print_list):
        if idx == len(print_list)-1:
            print(item)
        else:
            print(item, end = " ")

N,M,V = map(int, input().split())
#initialize graph
graph = {}
for num in range(N):
    graph[num+1] = []

for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)


dfs(graph,V)
bfs(graph,V)
