#Four-Coloring
#류채은
#16746
import copy

def bfs_based_coloring(graph):
    def is_adjacent(node1, node2):
        if node1 in graph[node2]:
            return True
        else:
            return False
    colors = [1,2,3,4]
    nodes_color = [0 for _ in range(len(graph.keys())+1)]

    red = 1
    green = 3
    blue = 4
    yellow = 2
                    

    visit = []
    queue = []
    start_node = list(graph.keys())[0]
    queue.append(start_node)
    left_colors = copy.deepcopy(colors)
    n_visited = 0
    while len(queue)!=0:
        node = queue.pop(0)
        if node not in visit:
            #visit node
            print(f"visiting node:{node}")
            print(nodes_color[1:])
            n_visited+=1
            visit.append(node)
            adjacent_nodes = graph[node]
            if n_visited <= 4:
                if len(left_colors) != 0:
                    left_color = left_colors.pop(0)
                    print(f"<=2>>colored: {left_color}")
                    nodes_color[node] = left_color
            else:
                
                left_colors = copy.deepcopy(colors)
                
                for adjacent in adjacent_nodes:
                    if nodes_color[adjacent] != 0:
                        adjacent_node_color = nodes_color[adjacent]
                        if adjacent_node_color in left_colors:
                            if adjacent_node_color == red:
                                where_red = adjacent
                            elif adjacent_node_color == blue:
                                where_blue = adjacent
                            elif adjacent_node_color == green:
                                where_green = adjacent
                            elif adjacent_node_color == yellow:
                                where_yellow = adjacent
                            print(f"cannot color(connected to {adjacent}): {adjacent_node_color}")
                            left_colors.remove(adjacent_node_color)
            
                if len(left_colors) != 0:
                    left_color = left_colors.pop(0)
                    nodes_color[node] = left_color
                    print(f"node{node} can be colored:{left_color}")
                else:
                    print("ALERT!!")
                    print("ALERT!!")
                    print("ALERT!!")
                    print("ALERT!!")
                    print("ALERT!!")
                    print("ALERT!!")
                    print(">>>>>changing...")
                    print("before:",nodes_color[1:])
                    print(f"yellow({yellow}) node:{where_yellow}, green({green}) node: {where_green} red({red}) node:{where_red} blue({blue}) node: {where_blue}")
                    if is_adjacent(where_red,where_green) == True:
                        
                        if is_adjacent(where_blue,where_red) == True:
                            print(f"changed node{where_red}: {red}->{yellow}")
                            nodes_color[where_red] = yellow
                        else:
                            print(f"changed node{where_red}: {red}->{blue}")
                            nodes_color[where_red] = blue
                        
                        nodes_color[node] = red
                        print("after:",nodes_color[1:])
                    else:
                        print(f"changed node{where_red}: {red}->{green}")
                        nodes_color[where_red] = green
                        nodes_color[node] = red
                        print("after:",nodes_color[1:])
                        
                    
                                
            queue.extend(graph[node])
            
    return visit,nodes_color

import random
for _ in range(10):
    h = random.randint(5,12)
    w = random.randint(5,12)
    n_nodes = h*w
    node_coordinates = [None for _ in range(n_nodes+1)]


    #initialize graph
    graph = {}
    len_graph = {}

    for _ in range(n_nodes):
        graph[_+1] = []
        len_graph[_+1] = 0
    '''
    for _ in range(n_nodes):
        x,y = map(int, input().split())
        #node_coordinates[_+1] = (x,y)
    '''
    real_node_names = {}
    name = 1
    for i in range(h):#y
        for j in range(w):#x
            real_node_names[str(j)+str(i)] = name
            name +=1

    n_edges = 0
    for i in range(h):
        for j in range(w):
            x_cursor = [-1,1,0]
            y_cursor = [-1,1,0]
            my_name = real_node_names[str(j)+str(i)]
            for move_x in x_cursor:
                for move_y in y_cursor:
                    if move_x == 0 and move_y == 0:
                        continue
                    else:
                        adj_name = str(j+move_x)+str(i+move_y)
                        if adj_name in list(real_node_names.keys()):
                            real_adj_name = real_node_names[adj_name]
                            if real_adj_name > my_name:
                                n_edges+=1
                                graph[my_name].append(real_adj_name)
                                graph[real_adj_name].append(my_name)
            

    assert n_nodes <= n_edges, print(f"n_nodes:{n_nodes} n_edges:{n_edges}")

    print("graph:",graph)

    visit, nodes_colors = bfs_based_coloring(graph)


    nodes_color = nodes_colors
    for value in nodes_color[1:]:
        print(value)

    for node, color in enumerate(nodes_color):
        adj_list = graph[node]
        for adj in adj_list:
            assert nodes_color[adj] != nodes_color[node]
                                       
