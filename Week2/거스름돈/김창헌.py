money = [500, 100, 50, 10, 5, 1]
N = int(input())
N = 1000 - N
answer = 0
for i in money:
  answer += N // i
  N = N % i

print(answer)