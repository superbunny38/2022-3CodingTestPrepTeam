n, m = map(int,input().split())
room = [list(input())for _ in range(n)]

ans = 0
def dfs(i, j):
    if room[i][j] == '-':
      room[i][j] = 0 # 0은 방문 처리한 것을 말하고 이후 조건문에서 해당 값은 무시된다. 즉 - 혹은 | 값을 인지하여 연속되는 값이 끝난 경우에 ans에 +를 하고 다시 조회하기를 반복하여 전체 값을 깉이 우선으로 탐색하는 것이다.
      if j < m - 1 and room[i][j+1] == '-':
        dfs(i, j + 1)
    elif room[i][j] == '|':
      room[i][j] = 0
      if i < n - 1 and room[i+1][j] == '|':
        dfs(i + 1, j)
    
    
for i in range(n):
    for j in range(m):
        if room[i][j]: # if 값은 0을 제외한 모든 값이 일단 true이다. 그렇기에 제일 처음은 무조건 +1이 된체 room을 순회하게 된다.
            ans += 1
            dfs(i, j)
print(ans)