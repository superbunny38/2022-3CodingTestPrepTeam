
def check(word):
    save = dict()
    prev = None
    for w in word:
        if prev == None:#첫 단어
            prev= w
            save[prev]=1
        else:
            if w in save and prev != w:
                return False
            else:
                save[w] = 1
                prev = w
    return True

N = int(input())
answer = 0
for _ in range(N):
    word = input()
    if check(word) == True:
        answer+=1
print(answer)
