def main():
    n = int(input())
    stairs = [int(input()) for _ in range(n)]
    maxScore = solve(n, stairs)
    print(maxScore)
    
def solve(n, stairs: list) -> int:
    '''
    300개 이하라 dfs로는 시간초과
    3연속 x, 3단 이상 x -> 2차원 dp 테이블?
    1개의 element 씩만 있다면 현재는 최대 값이라도 3연속 x 제한으로 실제 최대가 아닐 수 있음
    -> 1, 2연속 뿐이니 element 최대 2개씩 가지고 있기
    
    ac 받긴 했는데 뭔가 풀이가 구린 것 같음...
    '''
    if n == 1:
        return stairs[0]
    
    score = [[] for _ in range(n + 1)]
    score[0], score[1] = [[0, 0]], [[stairs[0], 1]] # [점수, 연속]
    for i in range(2, n + 1):
        currScore = stairs[i - 1]
        
        for  prevScore, cnt in score[i - 1]: # 한 단계 올라가기
            if cnt == 2: 
                continue
            score[i].append([prevScore + currScore, 2])
 
        prev = max(score[i - 2], key=lambda x: x[0]) # 두 단계 올라가기
        score[i].append([prev[0] + currScore, 1])
        
    return max(score[n], key=lambda x: x[0])[0]
    
main()