import sys


input = sys.stdin.readline
N = int(input())

baby = None  # 아기 상어
fishes = 0  # 남은 물고기들
space = None
dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]


# 물고기, 상어, 빈공간 분류
def Classification(s, i, j):  # s: 숫자, i: y좌표, j: x좌표
    global baby, fishes
    s = int(s)
    if s == 0:
        return None
    elif s == 9:
        baby = BabyShark(i, j)
        return baby
    else:
        global fishes
        fishes += 1
        fish = Fish(s, i, j)
        return fish


class Fish:  # 물고기
    def __init__(self, size, y, x, dist=0):
        self.size = size  # 사이즈
        self.loc = (y, x)  # 위치
        self.dist = dist  # 아기 상어와의 거리


class BabyShark(Fish):  # 아기 상어
    def __init__(self, y, x):
        super().__init__(2, y, x)  # 처음 크기는 2
        self.exp = 0  # 경험치
        self.time = 0  # 시간

    def __iter__(self):
        return self  # 이동 이후의 상어
    
    def __next__(self):  # 이동
        global space, fishes, N
        visited = [[False] * N for _ in range(N)]
        queue = [*self.loc, 0]  # 현재 위치, 거리
        target = Fish(0, N, N, N*N)  # 다음 먹이를 (N, N) 위치에 N 제곱의 거리로 초기화
        
        if fishes == 0:  # 먹을 물고기가 없으면
            raise StopIteration  # 중지

        while queue:  # BFS 탐색
            y, x, dist = queue.pop(0)
            if dist + 1 > target.dist:  # 다음 먹이 후보보다 거리가 커지면 멈춤
                break
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if (ny < 0) or (nx < 0) or (ny >= N) or (nx >= N) or (visited[ny][nx]):
                    continue
                visited[ny][nx] = True
                if space[ny][nx] is not None:  # 물고기가 있다면
                    fish = space[ny][nx]
                    if fish.size < self.size:  # 작은 물고기인 경우
                        # print(f'Candidate: {(ny, nx, dist + 1)}')
                        if fish.loc < target.loc:  # 타겟보다 더 위에, 더 왼쪽에 있으면
                            fish.dist = dist + 1
                            target = fish  # 갱신
                    elif fish.size == self.size:  # 크기가 같은 물고기인 경우
                        queue.append([ny, nx, dist + 1])  # 이동 가능함
                else:  # 빈 공간이면
                    queue.append([ny, nx, dist + 1])  # 이동 가능함
        
        if target.size > 0:  # 후보가 갱신됐다면 (물고기에게 이동 가능하면)
            self.move(*target.loc, target.dist)  # 이동
        else:
            raise StopIteration

    def move(self, i, j, dist):  # (i, j)에 거리가 dist인 곳으로 이동
        global space
        space[self.loc[0]][self.loc[1]] = None  # 아기 상어가 원래 있던 곳은 빈공간이 됨
        self.eat(space[i][j])  # 물고기를 먹는다
        self.time += dist  # 거리만큼 시간 증가
        
        # 아기 상어 좌표 갱신
        self.loc = (i, j)
        space[i][j] = self

    def eat(self, fish):  # 물고기 먹음
        global fishes
        fishes -= 1  # 남은 물고기 감소
        self.exp += 1  # 경험치 획득
        if self.exp == self.size:  # 본인 크기만큼 경험치가 쌓이면
            self.levelUp()  # 레벨 업
    
    def levelUp(self):
        self.exp = 0  # 경험치 초기화
        self.size += 1  # 사이즈 업
        

if __name__ == '__main__':
    space = [[Classification(s, i, j) for j, s in enumerate(input().split())] for i in range(N)]
    for i in baby:
        pass
    
    print(baby.time)