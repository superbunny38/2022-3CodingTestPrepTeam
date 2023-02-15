#문자열 폭발
string = input()
bomb = list(input())

#print("string:",string,"bomb:",bomb)

#분류가 스택이길래..
stack = []
bomb_length = len(bomb)
for s in string:
    stack.append(s)
    #print(stack[-bomb_length:])
    if len(stack)>=bomb_length and stack[-bomb_length:] == bomb:
        #print(">>exploded!\n")
        for _ in range(bomb_length):
            stack.pop(-1)

if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))
