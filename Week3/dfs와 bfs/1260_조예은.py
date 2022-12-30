import sys
from collections import deque


class Graph:
    def __init__(self, vertex, edge) -> None:
        self.vnum = len(vertex)  # the number of vertexs
        self.enum = len(edge)  # the number of edges
        self.vertex = vertex  # the list of vertexs
        self.edge = edge  # the list of edge
        self.adj = {v: set() for v in vertex}  # adjacent vertexs for each vertex
        
        for e in edge:
            self.adj[e[0]].add(e[1])
            self.adj[e[1]].add(e[0])

        self.adj = {v: sorted(adj) for v, adj in self.adj.items()}


def dfs(graph: Graph, v: int, visited: list(), search: list = list()):
    '''
    Depth-First Search
    
    v: int
        current vertex
    visited: List(bool)
        whether each vertex is visited or not
    search: list
        DFS result
    '''
    if not visited[v-1]:  # if not visited, visit.
        visited[v-1] = True
        search.append(v)
    for candidate in graph.adj[v]:  # visit adjacent vertexs
        if not visited[candidate-1]:  # not visited adjacent vertexs
            search = dfs(graph, candidate, visited, search)
    return search


def bfs(graph: Graph, v: int, search: list = list()):
    '''
    Breadth-First Search
    
    v: int
        current vertex
    search: list
        BFS result
    '''
    queue = deque()
    queue.append(v)
    while queue:
        v = queue.popleft()
        search.append(v)
        candidates = [v for v in graph.adj[v] if v not in (deque(search) + queue)]
        queue += candidates

    return search


if __name__ == '__main__':
    '''
    n: the number of vertexs
    m: the number of edges
    v: start vertex
    '''
    n, m, v = map(int, sys.stdin.readline().split())
    vertex = list(range(1, n+1))  # vertexs
    edge = list()  # edges
    for i in range(m):
        edge.append(list(map(int, sys.stdin.readline().split())))
    
    graph = Graph(vertex, edge)  # define graph
    print(*dfs(graph, v, [False]*n))
    print(*bfs(graph, v))