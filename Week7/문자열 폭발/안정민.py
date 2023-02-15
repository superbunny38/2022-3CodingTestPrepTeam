def solve(string, boom) -> str: # 1_000_000 <= nlogn
    stack = []
    n, m = len(string), len(boom)
    for s in string:
        stack.append(s)
        while boom == "".join(stack[-m:]):
            for _ in range(m):
                stack.pop()
    
    return "".join(stack) if stack else "FRULA"

string = input()
boom = input()

res = solve(string, boom)
print(res)