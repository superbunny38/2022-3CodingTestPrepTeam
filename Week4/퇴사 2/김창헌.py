import sys

input = sys.stdin.readline

T = int(input())
day = []
pay = []
dp = [0] * (T + 1)
for _ in range(T):
    a, b = map(int, input().split())
    day.append(a)
    pay.append(b)

k = 0
for i in range(T):
    k = max(k, dp[i])
    if day[i] + i > T:
        continue
    dp[day[i] + i] = max(k + pay[i], dp[day[i] + i])

# k는 현재 조회하는 인덱스의 dp 값과 전의 값을 비교하는 것으로
# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200
# 7일 경우 2일 날에 7일에 20원이 들어가있는데 1, 4, 5일을 거치면 45원이 들어가게된다.
# 이를 구하기 위하여 k를 조회하는 날의 dp값 1일에서 4일로 입력될때는 둘다 0이지만 1일의 pay가 더해진 값이 4일의 dp값인 0보다 크기에 dp[3]은 10이 입력되고 이후 4일을 조회했을때 k=10이 되고 4일의 페이인 20이 더해져 5일에는 30이 들어간다. 5일을 조회했을때 k값은 30이 되고 5일의 페이인 15와 더해져 45가 되면 이는 원래 값인 20보다 크기에 45가 들어가게 된다.
print(max(dp))
