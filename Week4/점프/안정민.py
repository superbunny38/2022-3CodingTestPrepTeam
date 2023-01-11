def main():
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    cnt = solve(n, board)
    print(cnt)
    
def solve(n, board) -> int:
    dir = [(1, 0), (0, 1)]
    
    visited = [[0] * n for _ in range(n)]
    visited[0][0] = 1
    for x in range(n):
        for y in range(n):
            jump = board[y][x]
            if jump == 0:
                continue
            for dx, dy in dir:
                tx, ty = x + jump * dx, y + jump * dy
                if not isRange(tx, ty, n):
                    continue
                visited[ty][tx] += visited[y][x]
        
    '''
    최대 n이 100이라 bfs로 2^100하면 메모리 초과
    visited 값을 dp처럼 추가하려니 나중에 접근하는 좌표의 값이 중복이 되지 않을까 했는데,
    생각해보니 조건처럼 되돌아가는 방향(좌, 상)이 없으면 순차적으로 2중 for문을 돌며 중복 x 
    '''
    return visited[-1][-1]

def isRange(x, y, n) -> bool:
    return 0 <= x < n and 0 <= y < n

main()