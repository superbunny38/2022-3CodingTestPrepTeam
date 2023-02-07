def getCntGroupWord(words):
    cnt = 0
    for word in words:
        cnt += int(isGroupWord(word))
    return cnt

def isGroupWord(word):
    charSet = set(word[0])
    for i in range(1, len(word)):
        prev, curr = word[i - 1], word[i]
        if prev == curr:
            continue
        elif curr in charSet:
            return False
        charSet.add(curr)
    return True

n = int(input())
words = [input() for _ in range(n)]
cnt = getCntGroupWord(words)
print(cnt)