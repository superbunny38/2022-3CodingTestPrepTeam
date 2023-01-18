from itertools import product


def search(minimum, apeach, n):
    # cases = list(product([True, False], repeat=10))
    maxscore = 0
    answer = [-1]
    for case in product([True, False], repeat=10):
        num = 0
        score = 0
        for i in range(10):
            if case[i]:
                num += minimum[9-i][0]
                score += minimum[9-i][1]
        if num > n:
            continue
        if score > apeach:
            remain = n - num
            if score > maxscore:
                maxscore = score
                answer = [minimum[x][0] if case[9-x] else 0 for x in range(10)]
                answer.append(remain)
    return answer


def solution(n, info):
    apeach = sum([10-i for i, num in enumerate(info) if num > 0])
    minimum = [[num+1, (10 - i if num == 0 else (10-i) * 2)] for i, num in enumerate(info)]
    answer = search(minimum, apeach, n)
    return answer

n = 5
info = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
print(solution(n, info))

# 첫 번째 핵심 아이디어
'''
어피치가 점수를 다 땄다고 가정하고 시작한다.
즉, 어피치가 [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0] 이면 10 + 9 + 8 + 7 = 34점을 갖고 있다.

라이언이 화살을 쏘면서 어피치의 점수를 빼앗는 대신, 2배의 점수를 가져간다.
즉, 라이언이 [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2] 이면 원래 규칙대로는
어피치: 34 - 10 = 24점, 라이언: 10점이지만
이 코드에서는 어피치는 그대로 34점인 대신, 라이언: 10 * 2 = 20점을 가져간다.

가장 큰 점수 차이는 어피치의 점수가 고정되었으므로 라이언의 점수가 가장 클 때이다.
'''

# 두 번째 핵심 아이디어
'''
라이언이 각 점수를 얻기 위해 최소 몇 발을 맞춰야 하는지 구한다.
= 어피치의 info에 각각 1씩 더하면 된다.

라이언이 점수를 얻어가는 모든 경우의 수를 구한다.
[T/F] * 10 => 2^10 = 1024가지
itertools의 product를 사용

product를 취했을 때, 
[(True, True, True), (True, True, False), (True, False, True), (True, False, False), (False, True, True), (False, True, False), (False, False, True), (False, False, False)]
이처럼 앞에서부터 (가장 큰 점수부터) 점수를 획득하게 된다.

따라서 점수와 product의 인덱스를 똑같이 가지 않고, (0점을 제외한) 9 - i로 인덱스를 계산해 가장 작은 점수부터 따지도록 한다.

각 경우마다 점수를 얻기 위해 최소 몇 발을 쐈는지 구하고 만약 n보다 크면 넘긴다. 또한 점수의 합이 어피치보다 낮으면 넘긴다. 점수의 합이 현재 최대 점수보다 큰 경우 answer와 최대 점수를 갱신한다.
'''