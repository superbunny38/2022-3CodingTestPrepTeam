import copy
def choose_dir(name, cur_alphabet):
    backward = 0
    forward = 0
    cur_index = name.index(cur_alphabet)
    backward_path = name[cur_index+1:]
    forward_path = name[:cur_index]
    
    for letter in name:
        if letter == 'A':
            backward +=1
            backward_path.remove(letter)
        else:
            break
    for letter in name[::-1]:
        if letter == 'A':
            forward +=1
            forward_path.remove(letter)
        else:
            break
    if backward>forward:
        return 'back', backward_path[::-1]
    else:
        return 'straight', forward_path
            

def shortest_alphabet_path(alphabet):
    db = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    right_cost = db.index(alphabet)
    left_cost = len(db)-right_cost
    return min(right_cost, left_cost)

def solution(name):
    print(f"\n\nNAME:{name} length: {len(name)}")
    name = list(name)
    move_cost = 0
    #alphabet cost
    for alphabet in name:
        cost = shortest_alphabet_path(alphabet)
        print(f"alphabet:{alphabet} cost: {cost}")
        final_cost += cost
        
    #move cost
    final_cost += move_cost    
    answer = final_cost
    return answer

'''
import random
for _ in range(90):
    db = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    length = random.randint(1,20)
    name = "".join(random.choices(db,k = length))
    print(solution(name))
    if solution(name) != real_solution(name):
        print("WRONG!!")
        print("WRONG!!")
        print("WRONG!!")
        print("WRONG!!")
        print("WRONG!!")
        break
    '''
    
