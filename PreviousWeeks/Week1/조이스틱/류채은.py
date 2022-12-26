#류채은
#조이스틱
            
def straight_forward(name):
  
    last_not_A = len(name)-1
    for idx,alphabet in enumerate(name[::-1]):
        if alphabet == 'A':
            continue
        else:
            last_not_A = (len(name)-1)-idx
            break
    return last_not_A

def straight_backward(name):

    dest_idx = 1
    for idx, alphabet in enumerate(name):
        if idx == 0:
            continue
        if alphabet == 'A':
            continue
        else:
            dest = alphabet
            dest_idx = idx
            break
    return (len(name) - dest_idx)

def shortest_alphabet_path(alphabet):
    db = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    right_cost = db.index(alphabet)
    left_cost = len(db)-right_cost
    return min(right_cost, left_cost)

def pivot_backward(name):
    pivotting_cost = len(name)
    for idx,alphabet in enumerate(name[::-1]):
        cur_idx = (len(name)-1)-idx
        before_idx = cur_idx-1
        if before_idx >= 0 and name[before_idx] == 'A':
            while before_idx >= 0 and name[before_idx] == 'A':
                before_idx -= 1
        dest_idx = before_idx
        pivotting_cost = min(pivotting_cost, (len(name)-cur_idx)*2+dest_idx)
    return pivotting_cost
        
def solution(name):
    print(f"\n\nNAME:{name} length: {len(name)}")
    name = list(name)
    final_cost = 0
    move_cost = 0
    pivotting_cost= len(name)
    #alphabet cost
    for idx,alphabet in enumerate(name):
        cost = shortest_alphabet_path(alphabet)
        print(f"alphabet:{alphabet} cost: {cost}")
        final_cost += cost

        #calculate pivotting
        next_idx= idx+1
        if next_idx<len(name) and name[next_idx] == 'A':
            while next_idx<len(name) and name[next_idx] == 'A':
                next_idx += 1
            dest_idx = next_idx
            pivotting_cost = min(pivotting_cost,2*idx+len(name)-dest_idx)
            
        
    #move cost
    print(f"alphabet cost: {final_cost}")
    straight_forward_cost = straight_forward(name)
    straight_backward_cost = straight_backward(name)
    pivot_backward_cost = pivot_backward(name)
    print(f"straight_forward_cost:{straight_forward_cost}")
    print(f"straight_backward_cost:{straight_backward_cost}")
    print(f"pivotting_cost:{pivotting_cost}")
    print(f"pivot_backward_cost:{pivot_backward_cost}")
    move_cost = min(straight_forward_cost, straight_backward_cost, pivotting_cost,pivot_backward_cost)
    final_cost += move_cost    
    answer = final_cost
    return answer
    

name = "JEROEN"
print(solution(name))
name = "JAN"
print(solution(name))
name = "JAZ"
print(solution(name))
name = "UKAAAAAAAAAATAAB"
print(solution(name))
name = "A"
print(solution(name))
print(real_solution(name))
name = "AB"
print(solution(name))
print(real_solution(name))
name = "ABCDAA"
print(solution(name))
name = "X"
print(solution(name))
name = "AAABABABABAAAAAAAAAAAAABBABABAA"
print(solution(name))
name = "AAABBAAAAAAAAAAAAAAAABABAA"
print(solution(name))
name = "BBBAAAB"
print(solution(name))
name = "ABABAAAAABA"
print(solution(name))
