def solution(number, k):
    print(f"\n\nNUMBER: {number} k:{k}")
    biggest_number = []
    n_remain = len(number)-k
    for idx, num in enumerate(number):
        print(f"\nnumber: {num}")
        print(f"stack: {biggest_number}")
        # print(f"num: {num}")
        if idx == 0:
            print(f"insert first number: {num}")
            biggest_number.append(num)
            continue
        if k ==0:
            print(f"k == 0, appending num: {num}")
            biggest_number.append(num)
            continue
        if biggest_number[-1] <= num:
            print("biggest_number[-1] <= num",biggest_number[-1] <= num)
            while len(biggest_number) != 0 and biggest_number[-1] < num and k>0:
                popped = biggest_number.pop(-1)
                print(f"erased: {popped}")
                k-=1
            print(f"appending: {num}")
            biggest_number.append(num)
        else:
            print("biggest_number[-1] <= num",biggest_number[-1] <= num)
            print(f"appending: {num}")
            biggest_number.append(num)
        # print(biggest_number)
        
    if len(biggest_number) != n_remain:
        biggest_number = biggest_number[:n_remain]
    answer = "".join(biggest_number)
    return answer

number = "13299149"
k = 4
print(solution(number,k))

number = "54298763"
k = 4
print(solution(number,k))
