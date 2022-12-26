#11558
#류채은

T = int(input())#테스트 케이스

test_case = []
for i in range(T):
    N = int(input())#플레이어 수
    tmp_test_case = [N]
    for j in range(N):
        tmp_test_case.append(int(input()))
    test_case.append(tmp_test_case)
#입력끝


    
for case in test_case:
    graph = {}
    for idx, value in enumerate(case):
        if idx == 0:
            N = value
        else:
            graph[idx] = value#학생 idx가 학생 value 지목

    start = 1
    count = 0
    found_J = False
    for _ in range(N):
        next = graph[start]
        #print(f"{start}가 지목: {next}")
        start = next
        count+=1
        if next == N:
            print(count)
            found_J = True
            break
    if found_J == False:   
        print(0)
        
