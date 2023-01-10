import sys


# DFS 탐색
def dfs(graph, s):
    while graph[s] != 0:     # 순환할 때까지 루프
        temp = graph[s] - 1  # 다음 숫자 저장
        graph[s] = 0         # 현재 숫자 방문 처리
        s = temp


if __name__ =='__main__':
    T = int(sys.stdin.readline())  # 테스트 케이스 개수
    
    for i in range(T):
        N = int(sys.stdin.readline())                         # 순열 크기 입력
        cycle = 0                                             # 순열 사이클 개수 0으로 초기화 
        graph = list(map(int, sys.stdin.readline().split()))  # 순열 입력
        for i in range(N):
            if graph[i] != 0:  # 방문 안한 숫자면 (새 순열 사이클 시작)
                cycle += 1     # 순열 사이클 개수 증가
                dfs(graph, i)  # DFS 탐색으로 사이클 방문 처리
        print(cycle)  # 순열 사이클 개수 출력