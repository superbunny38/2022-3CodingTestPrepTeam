import sys
sys.setrecursionlimit(10**8)  # DFS 런타임 에러 방지


dy = [-1, -1, -1, 0, 0, 1, 1, 1]  # 8방위
dx = [-1, 0, 1, -1, 1, -1, 0, 1]  # 8방위


# DFS 탐색
def dfs(island, w, h, y, x):
    for i in range(8):  # 인접한 방향 모두 탐색
        # 새 좌표 계산
        ny = y + dy[i]
        nx = x + dx[i]
        if (ny < 0 or nx < 0 or ny >= h or nx >= w):  # 새 좌표가 범위를 벗어났는지 확인
            continue
        if island[ny][nx] == 1:  # 새 좌표가 방문하지 않은 땅이면
            island[ny][nx] = -1  # 방문한다
            dfs(island, w, h, ny, nx)  # 재귀적으로 새 좌표를 탐색


if __name__ == '__main__':
    # 입력 크기가 (0, 0)이 나올 때까지 반복
    while True:
        w, h = map(int, sys.stdin.readline().split())  # 너비, 높이를 입력
        if (w == 0) & (h == 0):
            break
        num = 0  # 섬의 개수를 0으로 초기화
        
        # 섬이 표시된 지도를 입력받는다.
        island = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
        
        # 지도의 모든 좌표를 순회
        for i in range(h):
            for j in range(w):
                if island[i][j] == 1:  # 그 좌표에 땅이 있다면
                    island[i][j] = -1  # 방문한다
                    num += 1  # 섬의 개수를 증가
                    dfs(island, w, h, i, j)  # 인접한 땅 방문
        print(num)  # 섬의 개수를 출력