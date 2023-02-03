import sys

input = sys.stdin.readline
N = int(input())
room1 = [list(input().rstrip()) for _ in range(N)]
room2 = list(map(list, zip(*room1)))  # 전치
x = 0
y = 0


for i in range(N):
    for xsplit in ''.join(room1[i]).split('X'):
        if len(xsplit) >= 2:
            x += 1
    for ysplit in ''.join(room2[i]).split('X'):
        if len(ysplit) >= 2:
            y += 1
print(x, y)