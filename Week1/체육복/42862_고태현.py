def solution(n, lost, reserve):
    answer = n
    
    ##여벌 && 도난 교집합이라면 두 배열에서 삭제
    intersection = list(set(lost) & set(reserve))
    if intersection:     
        for i in intersection:
            lost.remove(i)
            reserve.remove(i)
    
    for i in reserve:
        left = i - 1
        right = i + 1
        if left in lost:
            lost.remove(left)
        elif right in lost:
            lost.remove(right)
    
    answer -= len(lost)         
            
                
    return answer
