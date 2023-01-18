# 답 봄, 시간 오래 걸림
import sys


input = sys.stdin.readline
s1, s2 = input().strip(), input().strip()

l1, l2 = len(s1), len(s2)
cache = [0] * l2

for i in range(l1):
    cnt = 0
    for j in range(l2):
        if cnt < cache[j]:
            cnt = cache[j]
        elif s1[i] == s2[j]:
            cache[j] = cnt + 1
print(max(cache))