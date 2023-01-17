from collections import deque

def main() -> None:
    src, dst = map(int, input().split())
    cnt = bfs(src, dst)
    print(cnt)

def bfs(src, dst) -> int:
    visited = set()
       
    dq = deque()
    dq.append((src, 0))
    while dq:
        now, time = dq.popleft()
        if now == dst:
            return time
        
        if now in visited or not isRange(now):
            continue
        visited.add(now)
        
        dq.append((now + 1, time + 1))
        dq.append((now - 1, time + 1))
        dq.appendleft((now * 2, time))
        
    return -1

def isRange(node):
    return 0 <= node < 200_000

main()