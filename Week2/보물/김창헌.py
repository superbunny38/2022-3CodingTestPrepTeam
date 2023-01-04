N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
answer = 0
A.sort()

for i in A:
  idx = B.index(max(B))
  temp = i * B[idx]
  answer += temp
  del B[idx]
  
print(answer)