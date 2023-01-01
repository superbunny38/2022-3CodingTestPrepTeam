import sys
from typing import List  # type annotation 빼면 시간 줄어들음 (dfs의 경우 160초-> 60초)
from collections import deque
class Country:  # 참전 국가
    def __init__(self, color: str) -> None:
        self.color = color
        self.power = 0


class Soldier:  # 병사
    def __init__(self, color: str) -> None:
        self.color = color
        self.visited = False


class Battlefield:  # 전쟁터
    def __init__(self, w: int, h: int, field: List[List[Soldier]]) -> None:
        self.width = w
        self.height = h
        self.field = field
        self.countries = dict()
        self.direction = [
            [-1, 0],  # up
            [0, 1],  # right
            [1, 0],  # down
            [0, -1],  # left
        ]
    
    def enter(self, colors: List[str]):  # 참전
        for color in colors:
            country = Country(color)
            self.countries.update({color: country})
    
    def possible(self, row, col):  # 가능한 좌표인가
        updown = 0 <= row < self.height
        leftright = 0 <= col < self.width
        return updown & leftright


def dfs(battlefield: Battlefield, row: int, col: int, num: int):  # 재귀로 방문
    soldier = battlefield.field[row][col]

    if not soldier.visited:
        soldier.visited = True
        num += 1

    for dir in battlefield.direction:
        next_row = row + dir[0]
        next_col = col + dir[1]
        if battlefield.possible(next_row, next_col):
            adj = battlefield.field[next_row][next_col]  # 인접한 병사
            if (not adj.visited) & (adj.color == soldier.color):  # 첫 방문이고, 같은 국가라면
                num = dfs(battlefield, next_row, next_col, num)
    return num


def bfs(battlefield: Battlefield, row: int, col: int, num: int):  # Queue를 이용해 방문
    queue = deque()
    soldier = battlefield.field[row][col]
    soldier.visited = True
    queue.append((row, col))
    while queue:
        row, col = queue.popleft()
        num += 1
        for dir in battlefield.direction:
            next_row = row + dir[0]
            next_col = col + dir[1]
            if battlefield.possible(next_row, next_col):
                adj = battlefield.field[next_row][next_col]
                if (not adj.visited) & (adj.color == soldier.color):
                    queue.append((next_row, next_col))
                    adj.visited = True
    return num


if __name__ == '__main__':
    '''
    n: int
        width of battlefield
    m: int
        height of battlefield
    '''
    n, m = map(int, sys.stdin.readline().split())
    matrix = [list(map(Soldier, sys.stdin.readline().strip('\n'))) for _ in range(m)]
    
    battlefield = Battlefield(n, m, matrix)
    battlefield.enter(['B', 'W'])
    for row in range(m):
        for col in range(n):
            soldier = battlefield.field[row][col]
            if not soldier.visited:
                # num = bfs(battlefield, row, col, 0)
                num = dfs(battlefield, row, col, 0)
                battlefield.countries[soldier.color].power += num**2

    our: Country = battlefield.countries['W']  # 아군
    enemy: Country = battlefield.countries['B']  # 적군
    print(our.power, enemy.power)