def main():
    n = int(input())
    paints = [list(map(int, input().split())) for _ in range(n)]
    minPrice = solve(n, paints)
    print(minPrice)
    
def solve(n, paints) -> int:
    for row in range(1, n):
        prevs = paints[row - 1]
        for col in range(3):
            prevMin = int(1e9)
            for i in range(3):
                if i == col:
                    continue
                prevMin = min(prevMin, prevs[i])
            paints[row][col] += prevMin
            
    return min(paints[-1])

main()