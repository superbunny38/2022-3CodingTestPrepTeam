#10451
#류채은
import copy

def count_cycle(arr):
    left = [_+1 for _ in range(len(arr))]
    arr = [0]+arr
    #print("arr:",arr)
    n_cycle = 0
    while True:
        if len(left) == 0:
            break
        start = left.pop(0)
        #print("start:",start)
        dest = arr[start]
        if start == dest:
            n_cycle +=1
            continue
        while start != dest:
            left.remove(dest)
            dest = arr[dest]
        n_cycle +=1
    return n_cycle
        

save_answer = []

T = int(input())#n test cases
for _ in range(T):
    N = int(input())
    array = list(input().split())
    array = [int(x) for x in array]
    answer = count_cycle(array)
    save_answer.append(answer)

for value in save_answer:
    print(value)
