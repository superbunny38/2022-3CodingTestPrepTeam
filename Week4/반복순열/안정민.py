def main() -> None:
    n, p = map(int, input().split())
    cnt = solve(n, p)
    print(cnt)

def solve(n, p) -> int:
    numDict = { n: 0 }
    
    cnt = 0
    now = n
    while True:
        next = getNextSeqNumber(now, p)
        if next in numDict:
            return numDict[next]

        numDict[next] = numDict[now] + 1
        now = next
        cnt += 1
        
def getNextSeqNumber(prev, p) -> int:
    nums = list(map(int, str(prev)))
    return sum(map(lambda x: x**p, nums))

main()