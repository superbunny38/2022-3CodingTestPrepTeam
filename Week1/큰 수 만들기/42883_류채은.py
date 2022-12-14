
import numpy as np
import sys
sys.setrecursionlimit(1000000)

def solution(number, k):
    # print(f"\n\nNUMBER: {number} pick {len(number)-k} digits\n")
    area = list(number)
    n_iters = len(number)-k
    answer = ""
    n_pick = len(number) - k
    
    for _ in range(n_iters):    
        if len(area) == n_pick:
            # print(f"adding on...{area}")
            answer = answer + "".join(area)
            break
        if n_pick == 1:
            answer += max(area)
            break
        no_access = area[-(n_pick-1):]
        to_choose_from = area[:-(n_pick-1)]
        # print(f"\nn_pick: {n_pick}")
        # print(f"area:{area}")
        # print(f"no access:{no_access}")
        # print(f"choose from:{to_choose_from}")
        picked = max(to_choose_from)
        # print(f"picked: {picked}")
        answer += str(picked)
        picked_idx = area.index(picked)
        area = area[picked_idx+1:]
        n_pick -= 1

    return answer



number = "1924"
k = 2
print(solution(number, k))

number = "1231234"
k = 3

print(solution(number, k))

number = "4177252841"
k = 4
print(solution(number, k))
