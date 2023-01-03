def main():
    n = int(input())
    count = solve(n)
    
    print(count % 10_007)
    return 0

def solve(n: int) -> int:
    
    ways = [0] * (n + 1)
    ways[0] = ways[1] = 1
    for i in range(2, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]
     
    return ways[n]

main()
