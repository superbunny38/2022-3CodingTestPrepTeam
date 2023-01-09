from collections import deque


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(maps):
    queue = deque()
    queue.append([0, 0, 1])
    n, m = [len(maps), len(maps[0])]
    
    while queue:
        y, x, cell = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (ny == n-1) & (nx == m-1):
                return cell + 1
            if (ny < 0) | (nx < 0) | (ny >= n) | (nx >= m):
                continue
            if maps[ny][nx] == 1:
                maps[ny][nx] = 0
                queue.append([ny, nx, cell + 1])
    return -1


def solution(maps):
    answer = bfs(maps)
    return answer


if __name__ == '__main__':
    maps = 	[[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]
    answer = solution(maps)
    print(answer)