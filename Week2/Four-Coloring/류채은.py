#Four-Coloring
#16746
import copy

def bfs_based_coloring(graph):
    colors = [1,2,3,4]
    nodes_color = {}
    
    #initialize node colors with 0
    for key in graph.keys():
        nodes_color[key] = 0
        
    save_nodes_color = [nodes_color]   
    visit = []
    queue = []
    start_node = list(graph.keys())[0]
    queue.append(start_node)

    n_visited = 0
    while len(queue)!=0:
        node = queue.pop(0)
        if node not in visit:
            #visit node
            n_visited+=1
            visit.append(node)
            print(f"\nvisiting {n_visited}th node: {node}")
            print(f"len(save_nodes_color):",len(save_nodes_color))
            print("save_nodes_color:",save_nodes_color)
            for _ in range(len(save_nodes_color)):
                nodes_color = save_nodes_color.pop(0)
                print("popped:",nodes_color)
                adjacent_nodes = graph[node]
                left_colors = copy.deepcopy(colors)
                for adjacent in adjacent_nodes:
                    if nodes_color[adjacent] != 0:
                        adjacent_node_color = nodes_color[adjacent]
                        if adjacent_node_color in left_colors:
                            print(f"cannot color(connected to {adjacent}): {adjacent_node_color}")
                            left_colors.remove(adjacent_node_color)
                if n_visited <= 2:
                    if len(left_colors) != 0:
                        left_color = left_colors.pop(0)
                        print(f"<=2>>colored: {left_color}")
                        nodes_color[node] = left_color
                        save_nodes_color.append(nodes_color)
                else:
                    if len(left_colors) != 0:
                        for left_color in left_colors:
                            tmp_nodes_color = copy.deepcopy(nodes_color)
                            tmp_nodes_color[node] = left_color
                            print(f"node{node} can be colored:{left_color}")
                            print(f"nodes_color:",tmp_nodes_color)
                            save_nodes_color.append(tmp_nodes_color)
                queue.extend(graph[node])
            
    return visit,save_nodes_color
    
    
n_nodes, n_edges = map(int, input().split())
#node_coordinates = [None for _ in range(n_nodes+1)]

#initialize graph
graph = {}
for _ in range(n_nodes):
    graph[_+1] = []

for _ in range(n_nodes):
    x,y = map(int, input().split())
    #node_coordinates[_+1] = (x,y)

for _ in range(n_edges):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

visit, nodes_colors = bfs_based_coloring(graph)
print("\n\npossible answers:")

for subset in nodes_colors:
    print(subset.values())

nodes_color = nodes_colors[0]
#print(nodes_color)
for value in list(nodes_color.values()):
    print(value)
