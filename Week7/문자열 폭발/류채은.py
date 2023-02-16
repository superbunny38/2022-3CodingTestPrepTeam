<<<<<<< HEAD
entire_string = input()
bomb = input()
=======
#문자열 폭발
string = input()
bomb = list(input())
>>>>>>> 73347f8d263ff1b19d41632e7c500448ea6bc042

#print("string:",string,"bomb:",bomb)

<<<<<<< HEAD
#알고리즘 분류에 스택이라고 적혀있어서..

stack = []
=======
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
>>>>>>> 73347f8d263ff1b19d41632e7c500448ea6bc042
