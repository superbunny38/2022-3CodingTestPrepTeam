from itertools import permutations
import copy
#메모리초과

def order(combi,S):
    tmp_S = copy.deepcopy(S)
    for c in combi:
        if c== '1':
            tmp_S +='A'
            #print("option1:",tmp_S)
        elif c== '2':
            tmp_S = tmp_S[::-1]+'B'
            #print("option2:",tmp_S)
    #print("returning:",tmp_S)
    return tmp_S
            
            

def convert_S_to_T(S,T):
    answer = 0
    n_addA = T.count('A') - S.count('A')#option1: 2
    n_addB = T.count('B') - S.count('B')#option2: 1
    t_sub_s = [x for x in T if x not in S]
    for combi in set(list(permutations(['1']*n_addA+['2']*n_addB,n_addA+n_addB))):
        #print("order:",combi)
        if order(combi,S) == T:
            return 1
    return 0

    
    return answer

S = input()#B
T = input()#ABBA
print(convert_S_to_T(S,T))
