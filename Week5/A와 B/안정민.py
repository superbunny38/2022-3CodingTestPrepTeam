def main() -> None:
    a, b = input(), input()
    res = solve(a, b)
    print(res)
    return

def solve(a, b) -> int:
    now = list(b)
    while len(now) > len(a):
        if now[-1] == "A":
            now.pop()
        elif now[-1] == "B":
            now.pop()
            now = now[::-1]
        
    return 1 if a == "".join(now) else 0

main()