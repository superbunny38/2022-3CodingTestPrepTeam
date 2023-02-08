from collections import deque

# import sys
# input=sys.stdin.readline()
# 0, 1, 2, 3 : 북, 동, 남, 서
#dx=[0, 1, 0, -1]
#dy=[1, 0, -1, 0]
# 왼쪽으로 돌리면 서, 남, 동, 북  : 3, 2, 1, 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


# 지도의 각 칸은 (r, c) =(y, x)
# 현재 위치 청소
# 현재 위치에서 왼쪽 방향부터 차례대로 탐색을 진행
# 왼쪽 방향에 청소할 수 있다면, 그 방향으로 회전한 다음 한 칸 전진
# 왼쪽 방향에 청소할 수 없다면, 그 방향으로 회전한 다음 왼쪽 방향 탐색
# 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는 바라보는 방향을 유지한채로 한 칸 후진한 다음 왼쪽방향 탐색
# 네방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우는 작동 멈춤

# 입력
# 1. 세로크기 N, 가로크기 M
# 2. 로봇청소기가 있는 칸의 좌표 (r, c), 바라보는 방향 d (0, 1, 2, 3)=(북, 동, 남, 서)
# 3. N개의 줄에 장소의 상태가 북쪽부터 남쪽, 서쪽부터 동쪽 순서대로 주어짐. 빈 칸은 0, 벽은 1로 주어진다.
#    지도의 첫행, 마지막행, 첫열, 마지막열에 있는 모든 칸은 벽이다.


def bfs(y, x, d):
    q = deque()
    # 시작 좌표(y,x) 삽입 및 visited 표시
    q.append([y, x, d])
    # 현재 위치를 청소
    cnt = 1
    # visited=[[False]*M for _ in range(N)]
    visited[y][x] = 2

    # queue에 값이 존재하는 동안 반복
    while q:
        sy, sx, sd = q.popleft()
        # 현재 위치에서 왼쪽부터 차례대로 인접한 칸을 탐색 # 왼쪽방향 탐색 : 북, 동, 남, 서 -> 서, 북, 동, 남
        for d in ((sd - 1) % 4, (sd - 2) % 4, (sd - 3) % 4, sd):
            # 왼쪽으로 회전하여 전진한 값을 저장
            ny = sy + dy[d]
            nx = sx + dx[d]

            if visited[ny][nx]==0:  # 청소 안했으면 그 방향으로 회전한 다음 한칸 전진하고 1번
                visited[ny][nx] = 2
                cnt += 1
                q.append([ny, nx, d])
                break

        # 네 방향 모두 집입 못한경우 : 뒤로 한칸 이동
        else:
            ny = sy - dy[sd]
            nx = sx - dx[sd]
            if visited[ny][nx] == 1:
                print(cnt)
                return
            else:
                q.append([ny, nx, sd])


N, M = map(int, input().split())
r, c, d = map(int, input().split())
visited = [list(map(int, input().split())) for _ in range(N)]
bfs(r, c, d)


# 그냥 구현으로 푼 경우
# 로봇 청소기
n, m = map(int, input().split())
r, c, direc = map(int, input().split())
dr=[-1, 0, 1, 0] #북동남서
dc=[0, 1, 0, -1]
board = [list(map(int, input().split())) for _ in range(n)] #벽은 1, 빈칸은 0
visited=[[0]*m for _ in range(n)] # 방문은 1, 미방문은 0

#현재 위치를 청소한다.
visited[r][c]=1 #현재 있는 위치는 청소를 했으니까
cnt=1 #청소한 횟수 : 현재 있는 위치는 청소를 했으니까
turn_time = 0 #회전한 횟수

while True:
    #현재 위치에서 왼쪽방향부터 탐색
    direc=(direc-1)%4
    nr=r+dr[direc]
    nc=c+dc[direc]
    #왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 한칸 전진후 다시 왼쪽반향 탐색
    if visited[nr][nc]==0 and board[nr][nc]==0:
        visited[nr][nc]=1
        r=nr
        c=nc
        cnt+=1
        turn_time=0
        continue
    else: #왼쪽방향에 청소할 공간이 없다면 그방향으로 회전하고 다시 왼쪽방향 탐색
        turn_time+=1
    if turn_time==4: #네방향이 모두 이미 청소 되어 있거나 벽이면서, 뒤쪽 방향이라도 후진할수 없는 경우는 작동을 멈춘다.

        nr = r - dr[direc]
        nc = c - dc[direc]
        if board[nr][nc] == 0:
            r=nr
            c=nc
        else:
            break
        turn_time=0
print(cnt)
