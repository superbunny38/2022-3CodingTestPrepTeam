
def solution(people, limit):
    print(f"\n\nPEOPLE: {people}, LIMIT:{limit}")
    n_ones = 0
    n_twos = 0
    sorted_people = sorted(people)
    left_idx = 0
    right_idx = len(people)-1
    two_boats = []
    one_boats = []
    while left_idx<=right_idx:
        if left_idx == right_idx:
            one_boats.append(sorted_people[left_idx])
            n_ones+=1
            break
        if sorted_people[left_idx]+sorted_people[right_idx] <= limit:
            two_boats.append([sorted_people[left_idx], sorted_people[right_idx]])
            n_twos+=1
            left_idx+=1
            right_idx-=1
        else:
            one_boats.append(sorted_people[right_idx])
            n_ones+=1
            right_idx -=1
    print("one boats:",one_boats)
    print("two boats:", two_boats)
    print(f"n_ones:{n_ones} n_twos:{n_twos}")
    answer = n_ones+n_twos
    return answer

people = [70, 50, 80, 50]
limit = 100
print(solution(people, limit))

people = [70, 80, 50]
limit = 100
print(solution(people, limit))

people = [70]
limit = 100
print(solution(people, limit))


people = [100]
limit = 100
print(solution(people, limit))


people = [40,60]
limit = 100
print(solution(people, limit))
