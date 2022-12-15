## 너무 오래 고민해서 구글링 풀이 참고

def solution(name):
    
    min_move = len(name) - 1
    answer = 0
    for idx,val in enumerate(name):
        ## 위아래 먼저
        answer += min(ord(val)-ord('A'), ord('Z')-ord(val)+1)
        
        next = idx + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        min_move = min([min_move, 2 *idx + len(name) - next, idx + 2 * (len(name) -next)])
    
    answer += min_move
    return answer