def main() -> None:
    n = int(input())
    seqList = []
    for _ in range(n):
        temp = list(map(int, input().split()))
        temp.append(0)
        seqList.append(temp)
    
    maxSum = solve(seqList)
    print(maxSum)

def solve(seqList: list) -> int:
    for seqIdx in range(1, len(seqList)):
        prevSeq = seqList[seqIdx - 1]
        currSeq = seqList[seqIdx]
        for numIdx, num in enumerate(currSeq[:-1]):
            currSeq[numIdx] = max(currSeq[numIdx], num + prevSeq[numIdx], num + prevSeq[numIdx - 1])
    
    return max(seqList[-1])

main()