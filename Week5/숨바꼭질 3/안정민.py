from collections import deque
import heapq

def main() -> None:
    src, dst = map(int, input().split())
    # cnt = bfs(src, dst)
    cnt = dijkstra(src, dst)
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

def dijkstra(src, dst) -> int:
    INF = int(1e9)
    hq = []
    times = [INF] * 200_000
    times[src] = 0
    heapq.heappush(hq, (0, src)) # time, node
    while hq:
        time, now = heapq.heappop(hq)
        if times[now] < time:
            continue
        
        candidates = (time + 1, now + 1), (time + 1, now - 1), (time, now * 2)
        for candi in candidates:
            t, next = candi
            if not isRange(next):
                continue
            
            if t < times[next]:
                times[next] = t
                heapq.heappush(hq, (t, next))
        
    return times[dst]

def isRange(node):
    return 0 <= node < 200_000

main()