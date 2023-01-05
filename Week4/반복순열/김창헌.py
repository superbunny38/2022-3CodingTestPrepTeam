A, P = map(int, input().split())
dp = [A]
same = 0

while same == 0:
  num = 0
  for j in str(dp[-1]):
    num += int(j)**P
  if num in dp:
    same = num
    break
  dp.append(num)

print(dp.index(same))
