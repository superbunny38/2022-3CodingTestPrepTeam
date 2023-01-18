def compare(arr1, arr2):  # 가장 낮은 점수를 더 많이 맞혔는지 비교
    idx = 10
    while idx >= 0 :
        if arr1[idx] > arr2[idx] :
            return 1
        elif arr1[idx] < arr2[idx] :
            return 0
        else :
            idx -= 1
    return -1

def cal(arr1, arr2) :  # 점수 계산
    res = 0
    for i in range(len(arr2)) :
        if arr1[i] > arr2[i] :
            res += 10 - i
        elif arr1[i] < arr2[i]:
            res -= (10 - i)
    return res

def dfs(info, idx, cand, arr, n) :
    if idx == 10 and n >= 0 :  # 마지막(0점) 과녁만 남고 화살이 0개 이상인 경우
        cur = arr + [n]  # 마지막 과녁에 남은 화살 다 쏜다
        total = cal(cur, info)  # 현재 경우의 점수 계산
        if total > cand[0] :  # 현 최고점보다 높은 경우 갱신
            cand[0] = total 
            cand[1] = cur
        elif total == cand[0] :  # 현 최고점과 같은 경우
            if compare(cur, cand[1]) :  # 비교
                cand[1] = cur
    if n < 0 or idx == 11:  # 화살 초과 or 과녁 초과면 끝
        return
    dfs(info, idx+1, cand, arr + [info[idx] +1], n - (info[idx] + 1))  # idx의 과녁을 맞추는 경우
    dfs(info, idx+1, cand, arr + [0], n)  # idx의 과녁을 맞추지 않는 경우

def solution(n, info):
    cand = [0, [0]*11]  # 후보: 점수, 화살 맞힌 개수(answer)
    dfs(info, 0, cand, [], n)  # 어피치 화살 맞힌 개수, 과녁 idx, 후보, 남은 화살 개수
    if cand[0] == 0 :
        return [-1]
    else :
        return cand[1]