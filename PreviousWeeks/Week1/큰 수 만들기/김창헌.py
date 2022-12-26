def solution(number, k):
    answer = []
    for num in number:
        # answer에 뭐라도 존재하고, k가 0보다 크며, answer의 맨 위 값이 현재의 num보다 작으면
        while answer and k > 0 and answer[-1] < num:
            # answer의 맨 위 값을 제거하고 k도 -1 해준다
            answer.pop()
            k -= 1
        # 현재의 num값은 무조건적으로 answer에 넣어준다
        answer.append(num)
    
# answer는 number의 길이 - k만큼 슬라이싱 해준다.
answer = ''.join(answer[:len(number)-k])
   
    return answer
