#15686
#치킨 배달
from itertools import combinations

def get_min_cost(save_dict,M):
    min_cost = 2*N*N*N
    for chicken_combi in list(combinations(save_dict[2],M)):
        #print("assessing chicken house combination:",chicken_combi)
        min_combi_cost=0
        #chicken_combi = possible chicken houses
        for house in save_dict[1]:
            cur_min_cost = 2*N
            house_y,house_x = house[0]+1,house[1]+1
            
            for chicken in chicken_combi:
                chicken_y,chicken_x = chicken[0]+1,chicken[1]+1 
                cur_min_cost = min(abs(house_y-chicken_y)+abs(house_x-chicken_x),cur_min_cost)
                #print(f"house({house_y},{house_x}) chicken({chicken_y},{chicken_x}):",abs(house_y-chicken_y)+abs(house_x-chicken_x))
                
            min_combi_cost += cur_min_cost
        #print("cost:",min_combi_cost)
        min_cost = min(min_cost,min_combi_cost)
    return min_cost
    

N,M = map(int, input().split())
graph = []#NxN
for _ in range(N):
    tmp_row = list(input().split())
    tmp_row = [int(x) for x in tmp_row]
    graph.append(tmp_row)


cost = [[0 for tmp in range(N)] for _ in range(N)]
save_dict = {1:[],2:[]}

for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:#치킨 
            save_dict[2].append([i,j])
        elif graph[i][j] == 1:#집
            save_dict[1].append([i,j])
print(get_min_cost(save_dict,M))      


