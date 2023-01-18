from collections import defaultdict


# 유저 아이디 리스트, 유저1 -> 유저2 신고 리스트 ["유저1 유저2", ...], 신고 k회 이상 받은 시 밴
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = set(report)
    reported = defaultdict(int)  # 각 유저가 신고 받은 횟수
    
    # 신고 받은 유저 체크를 위한 루프
    for r in report:
        reported[r.split()[1]] += 1
    
    # 신고 한 유저에게 메일을 보내기 위한 루프
    for r in report:
        i1, i2 = r.split()
        if reported[i2] >= k:
            answer[id_list.index(i1)] += 1
    return answer


'''
핵심 아이디어 1
report를 set으로 바꿔 중복 신고를 무시한다
'''

'''
핵심 아이디어 2
report는 신고한 유저, 신고 받은 유저의 정보가 담겨있고 이를 최대로 활용한다.

1) 신고 받은 유저 중심의 루프
- 신고 받은 유저를 기록한다. 몇 회 당했는지 dictionary에 기록

2) 신고 한 유저 중심의 루프
- 신고 한 유저에게 메일을 보낸다. 본인이 신고한 유저가 k회 이상 신고 받았을 경우 이메일을 보낸다.
'''