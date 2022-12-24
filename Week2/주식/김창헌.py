for _ in range(int(input())):
  N = int(input())
  ju = list(map(int, input().split()))
  ju.reverse()
  max = ju[0]
  answer = 0

  for i in range(1, N):
    if max < ju[i]:
      max = ju[i]
      continue
    answer += max - ju[i]
    
  print(answer)
