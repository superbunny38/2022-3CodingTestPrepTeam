def solution(id_list, report, k):
    answer = []#각 유저별로 처리 결과 메일을 받은 횟수
    report_dict = dict()
    n_reported = dict()
    
    for id in id_list:
        report_dict[id] = set()#id가 []에 저장된 id를 신고
        n_reported[id] = set()#id를 report 한 사람
        
    for r in report:
        user_id,reported_id = r.split()[0],r.split()[1]
        report_dict[user_id].add(reported_id)
        n_reported[reported_id].add(user_id)
        
    #print("report_dict:",report_dict)
    stopped = []
    for key,value in n_reported.items():
        n = len(value)
        if n >= k:
            stopped.append(key)
    
    for key,value in report_dict.items():#key = who reported, value = who got reported
        answer.append(len(set(stopped)&set(value)))           
    
        
    return answer
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list,report,k))

id_list = ["con", "ryan"]
report =["ryan con", "ryan con", "ryan con", "ryan con"]
k =3
print(solution(id_list,report,k))
