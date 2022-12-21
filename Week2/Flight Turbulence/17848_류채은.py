#17848
#Flight Turbulence
#류채은

n, m = map(int, input().split())
current_seats = input().split()
current_seats = [int(x) for x in current_seats]
current_seats = [None]+current_seats
moved_passengers = [0 for _ in range(n+1)]

want_to_move_to = current_seats[m]

while True:
    if m == current_seats[m]:
        break
    forcibly_moved = current_seats[want_to_move_to]#가고싶은 곳에 원래 있던 사람
    current_seats[want_to_move_to] = want_to_move_to#가고싶은 곳으로 배정
    print("moving:",forcibly_moved,"&",want_to_move_to)
    current_seats[m] = forcibly_moved
    moved_passengers[forcibly_moved]=1
    moved_passengers[want_to_move_to]=1
    if m != current_seats[m]:
        want_to_move_to = forcibly_moved
    else:
        break
print(sum(moved_passengers))
        
