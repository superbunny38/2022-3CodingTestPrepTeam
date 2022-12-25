#18535
#Tomb Raider

from itertools import product
import copy

def check_okay(graph_, way, dragon_list):
    way = list(way)
    n_rotate = -1
    dragon_idx = 0
    graph = copy.deepcopy(graph_)
    
    def h_check(graph, r_idx, c_idx, mode):#가로
        if mode == 'right':
            move = 1
            while c_idx + move < len(graph[0]):
                if graph[r_idx][c_idx+move] == '#':
                    return False
                elif c_idx+move == len(graph[0])-1 and graph[r_idx][c_idx+move] == '.':
                    return True
                elif graph[r_idx][c_idx+move] == '\\':
                    ans = v_check(graph,r_idx,c_idx+move,mode = 'bottom')
                    return ans
                elif graph[r_idx][c_idx+move] == '/':
                    ans = v_check(graph,r_idx,c_idx+move,mode = 'top')
                    return ans
                elif graph[r_idx][c_idx+move] == 'H':
                    return True
                move +=1
        elif mode == 'left':
            move = -1
            while c_idx + move >= 0:
                if graph[r_idx][c_idx+move] == '#':
                    return False
                elif c_idx+move == 0 and graph[r_idx][c_idx+move] == '.':
                    return True
                elif graph[r_idx][c_idx+move] == '\\':
                    ans = v_check(graph,r_idx,c_idx+move,mode = 'top')
                    return ans
                elif graph[r_idx][c_idx+move] == '/':
                    ans = v_check(graph,r_idx,c_idx+move,mode = 'bottom')
                    return ans
                elif graph[r_idx][c_idx+move] == 'H':
                    return True
                move -=1
            
    def v_check(graph, r_idx, c_idx, mode):#세로
        if mode == 'bottom':
            move = 1
            while r_idx + move < len(graph):
                if graph[r_idx+move][c_idx] == '#':
                    return False
                elif r_idx+move == len(graph)-1 and graph[r_idx+move][c_idx] == '.':
                    print("c_idx+move == len(graph)-1 return True")
                    return True
                elif graph[r_idx+move][c_idx] == '\\':
                    ans = h_check(graph,r_idx+move,c_idx,mode = 'right')
                    return ans
                elif graph[r_idx+move][c_idx] == '/':
                    ans = h_check(graph,r_idx+move,c_idx,mode = 'left')
                    return ans
                elif graph[r_idx+move][c_idx] == 'V':
                    print("V return True")
                    return True
                move +=1
                
        elif mode == 'top':
            move = -1
            while r_idx + move >= 0:
                if graph[r_idx+move][c_idx] == '#':
                    return False
                elif r_idx+move == 0 and graph[r_idx+move][c_idx] == '.':
                    return True
                elif graph[r_idx+move][c_idx] == '\\':
                    ans = h_check(graph,r_idx+move,c_idx,mode = 'left')
                    return ans
                elif graph[r_idx+move][c_idx] == '/':
                    ans = h_check(graph,r_idx+move,c_idx,mode = 'right')
                    return ans
                elif graph[r_idx+move][c_idx] == 'V':
                    return True
                move -=1
               
                
    '''
    #encode graph
    
    for r_idx, line in enumerate(graph):
        for c_idx, value in enumerate(line):
            if value == 'H' or 'V':#when meet dragon
                if way[dragon_idx] == 'R':#rotate
                    replace_to = list(set(['H','V'])-set([way[dragon_idx]]))[0]
                    graph[r_idx][c_idx] = replace_to
                    dragon_idx +=1
`   '''
    
    #encode graph
    for dragon,rotate in zip(dragon_list,way):
        row, col = dragon[0], dragon[1]
        if rotate == 'R':#Rotate
            replace_to = list(set(['H','V'])-set([graph[row][col]]))[0]
            graph[row][col] = replace_to
            
    print("encoded:")
    for g in graph:
        print(g)
    #check if graph follows the rule
    for dragon in dragon_list:
        row, col = dragon[0], dragon[1]
        print(f"dragon: (y:{row} x:{col})")
        if graph[row][col] == 'H':
            if h_check(graph,row,col,'right') == False:
                print("False (right)")
                return -1
            
            if h_check(graph,row,col,'left') == False:
                print("False (left)")
                return -1
            
        elif graph[row][col] == 'V':
            if v_check(graph,row,col,'top') == False:
                print("False (top)")
                return -1
            if v_check(graph,row,col,'bottom') == False:
                print("False (bottom)")
                return -1
            
    n_rotate = way.count('R')
    return n_rotate



n, m = map(int, input().split())
tomb_graph = []
dragon_list = []
for _ in range(n):
    line = list(input()[:m])
    for idx,l in enumerate(line):
        if l == 'H' or l == 'V':
            dragon_list.append((_,idx))
    tomb_graph.append(line[:m])

choices = ['R','O']#rotate or original
ways = list(product(choices,repeat = len(dragon_list)))

min_rotate = m*n+1

for way in ways:
    print("\nway:",way)
    n_rotate = check_okay(tomb_graph, way, dragon_list)
    print("n_rotate:",n_rotate)
    if n_rotate>0 and n_rotate<min_rotate:
        min_rotate = n_rotate
        
if min_rotate == m*n+1:
    min_rotate =-1
print(min_rotate)
