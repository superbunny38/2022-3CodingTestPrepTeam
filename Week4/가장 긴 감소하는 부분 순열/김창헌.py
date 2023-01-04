N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N
for i in range(1, len(arr)):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[j] + 1, dp[i])
            # dp[i]는 계속 앞의 값과 비교하면서 최대값을 구해야하는데, 만약 j가 여러 개고 그 값의 고저가 모두 다른 경우를 가정하면 앞의 j가 2라서 +1이 되어 dp[i] =3 일때 뒤의 j가 1이라 +1은 2인 상황이면 현재 자신의 dp[i]가 더 크기때문에 이를 구분할 max()함수가 필요한 것이다.
print(max(dp))
