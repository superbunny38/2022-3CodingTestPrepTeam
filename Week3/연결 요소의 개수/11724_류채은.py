#11724
#연결요소의개수

def dfs(graph, remaining_nodes):
    start_node = remaining_nodes[0]
    stack = [start_node]
    visited = []
    
    while stack:
        cur = stack.pop(-1)
        #print("cur:",cur)
        #print("visited:",visited)
        
        if cur in remaining_nodes:
            remaining_nodes.remove(cur)
            
        if cur not in visited:
            visited.append(cur)
            neighbors = graph[cur]
            for neighbor in neighbors:
                stack.append(neighbor)
    

graph = {}
N, M = map(int, input().split())

#graph initialization
for num in range(N):
    graph[num+1] = []
    
for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

remaining_nodes = list(graph.keys())
count = 0

while remaining_nodes:
    count +=1
    #dfs
    dfs(graph,remaining_nodes)
            
    
print(count)
