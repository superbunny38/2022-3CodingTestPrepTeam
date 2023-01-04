#16762
#류채은
#시간초과 걸림

import copy
def find_cow_w_one_friend(graph):
    save = []
    for cow in list(graph.keys()):
        if len(graph[cow]) == 1:
            save.append([cow])
    return save

def is_time_okay(new_way, time_const):
    for constraint in time_const:
        early, late = constraint[0], constraint[1]
        if early in new_way and late in new_way:
            early_idx = new_way.index(early)
            late_idx = new_way.index(late)
            if early_idx > late_idx:
                return False
        if late in new_way and early not in new_way:
            return False
    return True
    

N, M = map(int, input().split())

graph = {}
for _ in range(N):
    graph[_+1] = []
    
for _ in range(N-1):
    friend1, friend2 = map(int, input().split())
    graph[friend1].append(friend2)
    graph[friend2].append(friend1)

time_const = []#(early,late)
for _ in range(M):
    early, late = map(int, input().split())
    time_const.append([early,late])

ways = find_cow_w_one_friend(graph)

answers = [0 for _ in range(N+1)]

while ways:
    way = ways.pop(0)
    print("on way...:",way)
    
    tmp_graph = copy.deepcopy(graph)

    for already_out in way:
        #그래프에서 삭제
        adj_list = tmp_graph[already_out]
        for adj in adj_list:
            tmp_graph[adj].remove(already_out)
        del tmp_graph[already_out]
     
    #소 내보낸 후 남아있는 소 중 한 친구만 있는 소들 탐색
    if len(list(tmp_graph.keys())) == 2:#두 소만 남았을 때
        left_two = list(tmp_graph.keys())
        new_way = copy.deepcopy(way)
        new_way1 = new_way + left_two
        new_way2 = new_way + left_two[::-1]#거꾸로도 확인
        if is_time_okay(left_two, time_const) == True:#시간 확인
            print(new_way1)
            last = new_way1[-1]
            answers[last] = 1
        if is_time_okay(left_two[::-1], time_const) == True:
            print(new_way2)
            last = new_way2[-1]
            answers[last] = 1
        
    else:
        for cow in find_cow_w_one_friend(tmp_graph):
            new_way = copy.deepcopy(way)
            new_way+=cow
            if is_time_okay(new_way, time_const) == True:
                ways.append(new_way)

for idx, value in enumerate(answers):
    if idx == 0:
        continue
    else:
        print(value)
        
        
