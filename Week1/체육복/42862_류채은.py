#체육복
#류채은
import copy

def encode(n, lost, reserve):
    #-1: 빌려야 함 1: 빌려줄 수 있음 0:본인 것만 있음/처리할 필요 없
    bin_array = [0 for _ in range(n+1)]
    for r in reserve:
        bin_array[r] += 1
    for l in lost:
        bin_array[l] += -1
    return bin_array

def solution(n, lost, reserve):
    answer = 0
    min_n_lost = len(lost)
    way_stack = [encode(n,lost,reserve)]
    optimal_way = way_stack[0]
    while len(way_stack) != 0:
        #print(way_stack)
        way = way_stack.pop(0)
        for idx, value in enumerate(way):
            if idx == 0:
                continue
            if value == -1:
                if idx-1 >= 0 and way[idx-1] == 1 and idx+1<=n and way[idx+1] == 1:
                    way[idx] = 0
                    way1 = copy.deepcopy(way)
                    way1[idx-1] = 0
                    way_stack.append(way1)
                    way2 = copy.deepcopy(way)
                    way2[idx+1] = 0
                    way_stack.append(way2)
                    break
                elif idx-1 >= 0 and way[idx-1] == 1:
                    way[idx] = 0
                    way1 = copy.deepcopy(way)
                    way1[idx-1] = 0
                    way_stack.append(way1)
                    break
                elif idx+1 <= n and way[idx+1] == 1:
                    way[idx] = 0
                    way2 = copy.deepcopy(way)
                    way2[idx+1] = 0
                    way_stack.append(way2)
                    break
            if value == 1:
                if idx == n:
                    if way[idx-1] != -1:
                        way[idx] = 0
                else:
                    if idx-1 >=0 and way[idx-1] != -1 and idx+1<=n and way[idx+1] != -1:#빌려줄 곳이 없음
                        way[idx] = 0
        if way.count(1) == 0:
            n_lost = way.count(-1)
            if n_lost < min_n_lost:
                min_n_lost = n_lost
                optimal_way = way
    #print(optimal_way)
    answer = n-min_n_lost
    return answer

n = 5
lost = [2,4]
reserve = [1,3,5]
print(solution(n,lost,reserve))#5

n = 5
lost = [2,4]
reserve = [3]
print(solution(n,lost,reserve))#4

n = 3
lost = [3]
reserve = [1]
print(solution(n,lost,reserve))#2

n = 8
lost = [1,2,4,5,7]
reserve = [3,6,8]
print(solution(n,lost,reserve))#6

n = 1
lost = []
reserve = [1]
print(solution(n,lost,reserve))#1

n = 3
lost = [1,2,3]
reserve = [1,2]
print(solution(n,lost,reserve))#2

n = 3
lost = [1,2,3]
reserve = [1,2,3]
print(solution(n,lost,reserve))#3
