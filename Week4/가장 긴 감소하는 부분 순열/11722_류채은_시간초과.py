#11722
#가장 긴 감소하는 순열
#시간초
import copy

N = int(input())
num_array = list(input().split())
num_array = [int(x) for x in num_array]
num_array = num_array[:N]

save_stack = [[num_array[0]]]
max_len = 1

for idx, num in enumerate(num_array):
    if idx == 0:
        continue
    print("\nnum:",num)
    print("saved stacks:",save_stack)
    n_iter = len(save_stack)
    for _ in range(n_iter):
        stack = save_stack.pop(0)
        print("stack:",stack)
        max_ = stack[0]
        last = stack[-1]
        
        if max_len<len(stack):
            print("max length:",len(stack))
            max_len = len(stack)
            
        if max_<num and len(stack) != 1:#1
            print(f"1. appending to stack: [{num}]")
            save_stack.append([num])

        if num <last:#2
            stack.append(num)
            if max_len<len(stack):
                print("max length:",len(stack))
                max_len = len(stack)
            print(f"2. appending:",stack)
            save_stack.append(stack)
        
        elif num>last:#3
            '''
            if len(stack) == 1:
                save_stack.append(stack)
                continue
            save_stack.apppend(stack)'''
            if len(stack) != 1:
                stack_ = copy.deepcopy(stack)
                print(f"appending to stack: {stack}")
                save_stack.append(stack_)
                
            for value in stack[::-1]:
                if value<=num:
                    stack.remove(value)
                else:
                    break
            stack.append(num)
            
            if max_len<len(stack):
                print("max length:",len(stack))
                max_len = len(stack)
            
            if stack not in save_stack:
                print(f"3. appending:",stack)
                save_stack.append(stack)
        else:#4
            print(f"4. appending:",stack)
            save_stack.append(stack)
            
print(max_len)
