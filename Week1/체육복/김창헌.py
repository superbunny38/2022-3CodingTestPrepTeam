def solution(n, lost, reserve):
    lost_ = [r for r in lost if r not in reserve] 
    reserve_ = [l for l in reserve if l not in lost]
    # 반복문을 이용한 중복 제거 넣을 인자, 반복문, 조건문 순으로 들어간다.
    lost_.sort()
    reserve_.sort()
    # 효율적인 코드를 위해서 오름차순 정렬
    for i in reserve_:
# 오름차순으로 정렬했기에 빼기부터 검열
        if i-1 in lost_:
lost_.remove(i-1)
        elif i+1 in lost_:
          	lost_.remove(i+1)
            
    return n - len(lost_)
