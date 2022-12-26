def solution(number, k):
    aim = len(number)-k

###########시간초과 풀이#################
#     num = list(number)
#     for i in range(k):
#         for idx,val in enumerate(num):
#             #마지막 인덱스 전까지만
#             if idx != len(num)-1:
#                 #큰자리수부터 확인 후 다음 자리수보다 작으면 버림
#                 if val < num[idx+1]:
#                     num.remove(val)
#                     break
#####################################

    num = [] ##스택에 사용할 배열
    for n in number:
        while num and num[-1] < n and k > 0:
            num.pop()
            k-=1
        num.append(n)
    # 제거되지 않은 숫자가 있다면 뒤에서 삭제
    if len(num) != aim:
        num = num[:-(len(num)-aim)]
        
    answer = ''.join(num)
    return answer