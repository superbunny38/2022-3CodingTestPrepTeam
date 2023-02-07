import sys
from collections import defaultdict


dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]


class Student:
    def __init__(self, num, friends=list()):
        self.num = num
        self.friends = friends  # 내가 좋아하는 친구
        self.hooks = list()  # 나를 좋아하는 친구
        self.satisfy = 0
    
    def keep(self, student):
        self.hooks.append(student)


class Seat:
    def __init__(self, student=None, loc=None):
        self.student = student
        self.loc = loc
        self.near = 0  # 인접한 빈자리
        self.friends = defaultdict(int)  # 학생: 인접한 자리의 학생의 좋아하는 친구 수
        self.hooks = defaultdict(list)  # 학생: 인접한 자리의 학생을 좋아하는 친구


def arrangement(student, seats, N):
    maxCondition = [0, 0, -N, -N]
    for i in range(N):
        for j in range(N):
            seat = seats[N*i+j]
            if seat.student is None:
                now = [seat.friends[student], seat.near, -i, -j]
                if now > maxCondition:
                    maxCondition = now
    
    seat = seats[-N*maxCondition[2]-maxCondition[3]]  # 자리 결정
    student.satisfy += maxCondition[0]
    seat.student = student
    
    for i in range(4):
        ny = seat.loc[0] + dy[i]
        nx = seat.loc[1] + dx[i]
        if (0 <= ny < N) and (0 <= nx < N):
            nseat = seats[N*ny + nx]
            nseat.near -= 1
            if nseat.student is None:
                for hook in student.hooks:
                    nseat.friends[hook] += 1
                for friend in student.friends:
                    nseat.hooks[friend].append(student)
            else:
                if nseat.student in student.hooks:
                    nseat.student.satisfy += 1


input = sys.stdin.readline
N = int(input())
students = [Student(n+1) for n in range(N**2)]
num = [0] * (N**2)
seats = [Seat() for _ in range(N**2)]

for i in range(N):
    for j in range(N):
        near = 4
        if i == 0 or i == N-1:
            near -= 1
        if j == 0 or j == N-1:
            near -= 1
        n, *friends = list(map(int, input().split()))
        num[N*i + j] = n
        seat = seats[N*i + j]
        seat.loc = (i, j)
        seat.near = near
        student = students[n-1]
        student.friends = [students[friend-1] for friend in friends]
        for friend in friends:
            students[friend-1].keep(student)

for n in num:
    arrangement(students[n-1], seats, N)

satisfy = 0
for student in students:
    satisfy += round(10**(student.satisfy-1))
    
print(satisfy)