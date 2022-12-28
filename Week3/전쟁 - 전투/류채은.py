#1303
#전쟁-전투

def count_power(graph):
    start_x, start_y = 0,0
    move_x = [-1,1,0,0]
    move_y = [0,0,-1,1]

    route = [(start_x,start_y)]
    


N,M = map(int, input().split())
graph = []

for _ in range(N):
    tmp_row = input()
    graph.append(list(tmp_row))

count_power(graph)
