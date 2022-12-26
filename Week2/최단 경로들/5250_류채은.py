#5250
#최단경로들
#류채은
#시간초과 걸
import copy

class Graph:
    def __init__(self,n):
        self.adj = {}
        for i in range(n):
            self.adj[i+1] = []
        self.size = n

    def addEdge(self,u,v,w):
        self.adj[u].append([v,w])#dest and weight
        self.adj[v].append([u,w])

    def removeEdge(self,u,v):
        for neighbor in self.adj[u]:
            if neighbor[0] == v:
                to_remove = neighbor
        self.adj[u].remove(to_remove)
        
        for neighbor in self.adj[v]:
            if neighbor[0] == u:
                to_remove = neighbor
        self.adj[v].remove(to_remove)

    def getEdges(self, node):
        edges = []
        for neighbor in self.adj[node]:
            edges.append(neighbor[0])
        return edges

    def getWeight(self,dest,source):
        for neighbor in self.adj[dest]:
            if neighbor[0] == source:
                return neighbor[1]
        
    def dijkstra(self,initial,end):
        shortest_paths = {initial: (None,0)}
        current_node = initial
        visited = set()

        while current_node != end:
            visited.add(current_node)
            destinations = self.getEdges(current_node)
            weight_to_current_node = shortest_paths[current_node][1]

            for next_node in destinations:
                weight = self.getWeight(current_node,next_node) + weight_to_current_node
                if next_node not in shortest_paths:
                    shortest_paths[next_node] = (current_node, weight)
                else:
                    current_shortest_weight = shortest_paths[next_node][1]
                    if current_shortest_weight > weight:
                        shortest_paths[next_node] = (current_node, weight)
            next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
            if not next_destinations:
                return -1#root not possible

            current_node = min(next_destinations, key = lambda k: next_destinations[k][1])
        '''
        path = []
        while current_node is not None:
            path.append(current_node)
            next_node= shortest_paths[current_node][0]
            current_node = next_node

        path= path[::-1]
        print("w:",weight)
        '''
        return weight
                
    
# Get inputs
n,m,a,b = map(int, input().split())

# Create a graph
g = Graph(n)

for _ in range(m):
    u,v,w = map(int, input().split())
    g.addEdge(u,v,w)
    
last_line_input = list(input().split())
last_line_input = [int(x) for x in last_line_input]
k = last_line_input[0]
shortest_path = last_line_input[1:k+1]

for idx, remove_edge in enumerate(shortest_path):
    tmp_graph = copy.deepcopy(g)
    if idx != len(shortest_path)-1:
        source_remove = remove_edge
        dest_remove = shortest_path[idx+1]
        tmp_graph.removeEdge(source_remove,dest_remove)#도로 파괴
        w = tmp_graph.dijkstra(a,b)
        print(w)    


