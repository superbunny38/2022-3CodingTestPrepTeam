S = input()#B
T = input()#ABBA

answer = 0
while T:
    peek = T[-1]
    if peek == 'A':
        T = T[:-1]
    elif peek == 'B':
        T = T[:-1]
        T = T[::-1]
    if T == S:
        answer = 1

print(answer)
