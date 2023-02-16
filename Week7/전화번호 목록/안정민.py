import sys
input = sys.stdin.readline

def isValid(n, phones: list) -> bool:
    maxLen = 10
    phones.sort(key = lambda x: x + "0" * (maxLen - len(x)))
    for i in range(1, len(phones)):
        prev, curr = phones[i - 1], phones[i]
        if prev == curr[:len(prev)]:
            return False
    
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    phones = [input().strip() for _ in range(n)]

    res = "YES" if isValid(n, phones) else "NO"
    print(res)
    