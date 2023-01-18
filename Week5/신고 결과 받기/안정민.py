def solution(id_list, report, k):
    
    result = { id: 0 for id in id_list }
    reportedDict = { id: 0 for id in id_list }
    
    report = list(set(report))
    
    for re in report:
        _, reported = re.split()
        reportedDict[reported] += 1
        
    for re in report:
        reporter, reported = re.split()
        if reportedDict[reported] >= k:
            result[reporter] += 1

    return list(map(lambda x: result[x], id_list))