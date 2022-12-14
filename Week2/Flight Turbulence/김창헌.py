n, m = map(int,input().split())
seats = list(map(int, input().split()))
# m은 현재 지정좌석으로 이동하기 원하는 고객의 좌석 번호이다
# 4 4 / 2 3 4 1 일 경우
# 현재 4번 좌석의 손님이 1번 좌석인 자신의 좌석으로 가기를 원한다.
# 그렇다면 4번인 1번 지정좌석 손님이 1번으로 이동하기 위해 1번 좌석을 조회하면 
# 1 = seats[m-1] 이라는 식이 세워진다.
# 이 m값을 조회이자 이동이라고 가정하면 첫번째에서 m번째 손님은 자신의 좌석으로 이동한 것이다. 하지만 나머지 손님도 이동을 해야하는데 그렇다면 이동당하는 m번째 손님의 값은 seats[m-1]인 2가 된다. 
# 2번 손님은 자신의 좌석에 있는 3번 손님으로 이동하고 3번 손님은 자신의 자리에 있는 4번 손님의 조회하여 원래 있어야할 m번째 좌석의 손님이 해당 자리로 이동하게 된다고 말할 수 있다.

orig = m # 이후 m 좌석이 m번 지정 좌석인 손님이 잘 들어왔는지 확인하기 위함
cnt = 0

while seats[m-1] != orig: # 현재 좌석의 값과 m의 값이 같아질때까지 반복
    cnt += 1 # 한 번 조회가 한 번 이동이라고 가정
    m = seats[m-1] # 조회한 원래 자리로 이동한다.
  
if cnt == 0:
    print(0)
else:
    print(cnt + 1)