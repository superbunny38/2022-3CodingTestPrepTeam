from collections import deque
def bfs(y, x):
    q = deque()
    q.append((y, x))
    graph[y][x] = 0
    while q: # bfs에서는 queue를 사용하여 반복문을 이용해서 탐색을 한다.
        y, x = q.popleft()
        for dy, dx in d: # map 안의 xy를 모두 반복해서 탐색.
            Y, X = y+dy, x+dx
            if (0 <= Y < 10) and (0 <= X < 10):
                if graph[Y][X] == 'L':
                    return graph[y][x]
                if graph[Y][X] == '.':
                    q.append((Y, X))
                    graph[Y][X] = graph[y][x]+1 # 전의 값에 1을 더해서 cnt 값을 출력하기 위함.

graph = [list(input()) for _ in range(10)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(10):
    for j in range(10):
        if graph[i][j] == 'B':
            cnt = bfs(i, j)
print(cnt)