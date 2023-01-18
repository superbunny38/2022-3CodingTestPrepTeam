from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = set(report)
    reported = defaultdict(int)
    for r in report:
        reported[r.split()[1]] += 1
    
    for r in report:
        i1, i2 = r.split()
        if reported[i2] >= k:
            answer[id_list.index(i1)] += 1
    return answer