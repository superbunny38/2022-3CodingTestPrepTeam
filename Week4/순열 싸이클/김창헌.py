import sys
sys.setrecursionlimit(10**7)

def dfs(x, sig):
  sig[x] = True
  if sig[cycle[x]] == False:
    dfs(cycle[x], sig)
    
for i in range(int(input())):
  N = int(input())
  cycle = [0] + list(map(int,input().split()))
  sig = [False] * (N+1)
  ans = 0
  for i in range(1, len(cycle)):
    if sig[i] == False:
      dfs(cycle[i], sig)
      ans +=1
  print(ans)