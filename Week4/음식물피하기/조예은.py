import sys
from collections import deque # import에 시간 오래 걸림 (20초 정도)
sys.setrecursionlimit(10**8)  # DFS 런타임 에러 방지

n, m, k = map(int, sys.stdin.readline().split())  # 통로의 세로, 가로, 음식물 개수
trash = [[False] * m for _ in range(n)]  # 통로의 음식물 초기화

for _ in range(k):
    y, x = map(int, sys.stdin.readline().split())  # 음식물 있는 좌표
    trash[y-1][x-1] = True  # 음식물이 있다

dy = [0, 0, -1, 1]  # 우, 좌, 하, 상
dx = [1, -1, 0, 0]  # 우, 좌, 하, 상
size = 0  # 음식물 크기


# DFS 탐색
def dfs(y, x):
    global size
    for i in range(4):  # 인접한 방향 모두 탐색
        # 새 좌표 계산
        ny = y + dy[i]
        nx = x + dx[i]
        if (ny < 0 or nx < 0 or ny >= n or nx >= m):  # 새 좌표가 범위를 벗어났는지 확인
            continue
        if trash[ny][nx]:  # 새 좌표에 쓰레기가 있으면
            trash[ny][nx] = False  # 쓰레기를 치운다
            size += 1  # 음식물 크기를 증가
            dfs(ny, nx)  # 재귀적으로 새 좌표를 탐색


# BFS 탐색
def bfs(y, x):
    queue = deque([(y, x)])  # Queue에 초기 좌표를 넣는다.
    global size
    
    while queue:  # Queue가 빌 때까지 반복
        y, x = queue.popleft()  # Queue에서 현재 좌표를 꺼낸다
        for i in range(4):  # 인접한 방향 모두 탐색
            # 새 좌표 계산
            ny = y + dy[i]
            nx = x + dx[i]
            if (ny < 0 or nx < 0 or ny >= n or nx >= m):  # 새 좌표가 범위를 벗어났는지 확인
                continue
            if trash[ny][nx]:  # 새 좌표에 쓰레기가 있으면
                trash[ny][nx] = False  # 쓰레기를 치운다
                size += 1  # 음식물 크기를 증가
                queue.append((ny, nx))  # queue에 새 좌표 추가


if __name__ == '__main__':
    max_size = 0  # 음식물 최대 크기 0으로 초기화
    
    # 통로의 모든 좌표를 순회
    for i in range(n):
        for j in range(m):
            if trash[i][j]:  # 음식물이 있는지 확인
                trash[i][j] = False  # 음식물을 치운다
                size = 1  # 음식물 크기 1
                bfs(i, j)  # 탐색
                # dfs(i, j)
                max_size = max(size, max_size)  # 음식물 최대 크기 업데이트
    print(max_size)  # 음식물 최대 크기를 출력