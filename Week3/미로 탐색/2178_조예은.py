import sys
from collections import deque


n, m = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().strip('\n'))) for _ in range(n)]
direction = [
    [-1, 0],  # up
    [0, 1],  # right
    [1, 0],  # down
    [0, -1],  # left
]


def bfs(row, col):
    queue = deque()
    queue.append((row, col))
    
    while queue:
        row, col = queue.popleft()
        for dir in direction:
            next_row = row + dir[0]
            next_col = col + dir[1]
            if (0 <= next_row < n) and (0 <= next_col < m) and matrix[next_row][next_col] == 1:
                queue.append((next_row, next_col))
                matrix[next_row][next_col] = matrix[row][col] + 1
    return matrix[n-1][m-1]

if __name__ == '__main__':
    print(bfs(0, 0))