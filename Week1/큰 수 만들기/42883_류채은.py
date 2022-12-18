def solution(number, k):
    print(f"\n\nNUMBER: {number} k:{k}")
    biggest_number = []
    n_remain = len(number)-k
    for idx, num in enumerate(number):
        print(f"num: {num}")
        if idx == 0:
            biggest_number.append(num)
            continue
        if k ==0:
            biggest_number.append(num)
            continue
        if biggest_number[-1] <= num:
            while len(biggest_number) != 0 and biggest_number[-1] < num and k>0:
                biggest_number.pop(-1)
                k-=1
            biggest_number.append(num)
        else:
            biggest_number.append(num)
        print(biggest_number)
        
    if len(biggest_number) != n_remain:
        biggest_number = biggest_number[:n_remain]
    answer = "".join(biggest_number)
    return answer

number = "1924"
k = 2
print(solution(number,k))

number = "1231234"
k = 3
print(solution(number,k))

number = "4177252841"
k = 4
print(solution(number,k))

number = "5284192"
k = 1
print(solution(number,k))

number = "11"
k = 1
print(solution(number,k))

number = "31"
k = 1
print(solution(number,k))

number = "13"
k = 1
print(solution(number,k))
