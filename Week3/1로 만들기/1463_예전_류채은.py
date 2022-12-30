#1463
#1로 만들기

class Tree:
    def __init__(self, data,depth,parent):
        self.children = []
        self.parent = parent
        self.data = data
        self.depth = depth

def calculate_and_add_children(p_node,depth,explored):
    number = p_node.data
    children_list = []
    if number % 3 == 0:
        value = number/3
        if value not in explored.keys():
            #print("   adding child node... value: {} depth: {}".format(value, depth+1))
            if value == 1:
                return explored, depth+1
            three = Tree(value,depth+1,p_node.data)
            children_list.append(three)
    if number %2 == 0:
        value = number/2
        if value not in explored.keys():
            two = Tree(value,depth+1,p_node.data)
            #print("   adding child node... value: {} depth: {}".format(value, depth+1))
            if value == 1:
                return explored, depth+1
            children_list.append(two)
    if number -1 > 0:
        value = number -1
        if value not in explored.keys():
            minus = Tree(value,depth+1,p_node.data)
            #print("   adding child node... value: {} depth: {}".format(value, depth+1))
            if value == 1:
                return explored, depth+1
            children_list.append(minus)
    return explored, children_list

def eliminate_redundance(parent_keys):
    new_keys = []
    data = []
    for p in parent_keys:
        if p.data not in data:
            data.append(p.data)
            new_keys.append(p)
        else:
            continue
    return new_keys

def get_data(parent_keys):
    d = []
    for p in parent_keys:
        d.append(p.data)
    d = set(d)
    #print(d)
    return list(d)

def display_exploration(parent_keys):
    for p in parent_keys:
        print(p.data,end = " ")

def prune_level(parent_keys):
    new_keys = []
    
    for p in parent_keys:
        if p.data in get_data(new_keys):
            continue
        else:
            new_keys.append(p)
    return new_keys

def main():
    explored = dict()
    
    tmp_parent= []
    N = int(input())
    if N == 1:
        return 0
    explored[N] = 1
    root = Tree(N,0,None)
    parent_keys = [root]
    depth = 0
    for j in range(N-1):
        parent = parent_keys.pop()
        #print("\naccessed:",parent.data,"depth:",parent.depth,"parent:",parent.parent)
        explored[parent.data] = 1
        explored, c = calculate_and_add_children(parent,depth,explored)
        if type(c) == int:
            return c
        elif type(c) == list:
            if len(c) == 0:
                pass#do nothing
                #print("없애야함")
            else:
                parent.children = c
                tmp_parent += parent.children
        
        if len(parent_keys) == 0:
            depth+=1
            parent_keys = prune_level(tmp_parent)
            #print("\n\n(parent:{}) nodes to explore:".format(parent.data), end = " ")
            #display_exploration(parent_keys)
            tmp_parent = []
print(main())
