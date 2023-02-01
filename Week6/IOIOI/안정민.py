import re

def main():
    n = int(input())
    maxLen = int(input())
    target = input()
    cnt = solve4(n, maxLen, target)
    print(cnt)

# 단순 2중 for
def solve(n, maxLen, target) -> int:
    cnt = 0
    comp: str = "I" + "OI" * n
    for i in range(maxLen):
        if i + len(comp) > maxLen:
            break
            
        isMatch = True
        for j, x in enumerate(comp):                
            if i + j < maxLen and x != target[i + j]:
                isMatch = False
                break

        cnt += bool(isMatch)
            
    return cnt

# 정규식으로 찾아보기
def solve2(n, maxLen, target: str) -> int:
    cnt = 0
    compLen = 2 * n + 1
    reg = f"I(OI){{{n},}}"
    res = re.finditer(reg, target)
    for x in res:
        temp = len(x.group())
        cnt += (temp - compLen) // 2 + 1
    return cnt

def solve3(n, maxLen, target: str) -> int:
    cnt = 0
    comp = "I" + "OI" * n
    compLen = len(comp)
    idx = 0
    while idx < maxLen:
        if comp == target[idx:idx + compLen]: # 여기서 오래걸리는 것 같음
            idx += compLen
            while idx + 2 <= maxLen:
                if "OI" == target[idx: idx + 2]:
                    cnt += 1
                    idx += 2
                else:
                    break
            cnt += 1
        else:
            idx += 1

    return cnt

# 비교 단위를 comp가 아닌 IOI로
def solve4(n, maxLen, target: str) -> int:
    cnt = idx = repeat = 0
    
    while idx < maxLen:
        if "IOI" == target[idx:idx + 3]:
            idx += 2
            repeat += 1
            if repeat == n:
                cnt += 1
                repeat -= 1
        else:
            idx += 1
            repeat = 0
            
    return cnt

main()