import sys

class Game:
    def __init__(self, N, L, field, rotates):
        self.size = N  # 보드의 크기
        self.snake = Snake()  # 뱀
        self.field = field  # 보드
        self.rotates = rotates  # 방향 변환 정보
        self.num = L  # 방향 전환 횟수
        self.check = 0  # 방향 전환 횟수 기록
        self.turn = 1  # 턴
    
    def __iter__(self):
        return self
    
    def __next__(self):
        ny, nx = self.snake.move()  # 뱀 이동
        if (ny >= N or nx >= N or ny < 0 or nx < 0) or (field[ny][nx] == 2):  # 게임 오버
            raise StopIteration
        if field[ny][nx] == 0:  # 빈 공간
            oy, ox = self.snake.shorten()
            field[oy][ox] = 0
        field[ny][nx] = 2
        if self.check < self.num and (self.rotates[self.check][0] == str(self.turn)):  # 회전 체크
            self.snake.rotate(self.rotates[self.check][1])
            self.check += 1
        self.turn += 1


class Snake:
    def __init__(self):
        self.loc = [(0, 0)]  # 위치 기록
        self.dx = [1, 0, -1, 0]  # 시계방향
        self.dy = [0, 1, 0, -1]
        self.dir = 0  # 초기 진행 방향: 우측 (dx[0], dy[0])
        
    def move(self):  # 진행
        nx = self.loc[-1][1] + self.dx[self.dir]
        ny = self.loc[-1][0] + self.dy[self.dir]
        self.loc.append((ny, nx))
        return ny, nx
    
    def shorten(self):  # 몸 길이 줄임
        return self.loc.pop(0)

    def right(self):  # 오른쪽 회전
        self.dir = (self.dir + 1) % 4
    
    def left(self):  # 왼쪽 회전
        self.dir = (self.dir - 1) % 4

    def rotate(self, r):  # 회전
        if r == 'D':
            self.right()
        elif r == 'L':
            self.left()


if __name__ == '__main__':
    input = sys.stdin.readline
    N, K = int(input()), int(input())
    field = [[0] * N for _ in range(N)]
    field[0][0] = 2
    for _ in range(K):
        x, y = input().rstrip().split()
        field[int(x)-1][int(y)-1] = 1

    L = int(input())
    rotates = [input().rstrip().split() for _ in range(L)]
    
    game = Game(N, L, field, rotates)
    for _ in game:
        pass
    
    print(game.turn)