N = int(input())
people = list(map(int, input().split()))
answer = 0
people.sort()
while people:
  for i in people:
    answer += i
  people.pop()

print(answer)
