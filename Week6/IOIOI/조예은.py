import sys


input = sys.stdin.readline
N = int(input())
M = int(input())
S = input()

start = -1
end = M
cnt = 0
before = ''

for i in range(M):
    if start > -1 and before == S[i]:
        end = i
        # I 개수의 차 + 1 => (end - start + 1) // 2 - (N + 1) + 1
        cnt += max(0, (end - start + 1) // 2 - N)
        start = -1
        
    if start == -1 and S[i] == 'I':
        start = i
        end = M
    before = S[i]
    
if start != -1 and end == M:
    cnt += max(0, (end - start + 1) // 2 - N)

print(cnt)