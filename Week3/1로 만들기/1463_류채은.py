#1463
#1로 만들기
#시간초과 이렇게 푸는거 아닌듯

def min_make_one(N):
    count =0
    save_candidates= [N]
    while True:
        new_candidates = []
        while save_candidates:
            n = save_candidates.pop(0)
            if n%3 == 0:
                new_n = int(n/3)
                if new_n == 1:
                    return count+1
                new_candidates.append(new_n)
            elif n%2 == 0:
                new_n= int(n/2)
                if new_n == 1:
                    return count+1
                new_candidates.append(new_n)
            new_n = n-1
            if new_n == 1:
                return count+1
            new_candidates.append(new_n)
        count +=1
        save_candidates = new_candidates
    return count

N = int(input())
print(min_make_one(N))
