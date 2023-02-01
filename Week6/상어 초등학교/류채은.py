#new21608
#Chaeeun Ryu
import random

def print_pos(std_positions):
    for pos in std_positions:
        for idx, p in enumerate(pos):
            if idx != len(std_positions)-1:
                print(p, end = "")
            else:
                print(p)

def get_empty_seats(std_positions):
    #print("std_positions:",std_positions)
    empty_ = []
    n = len(std_positions)
    for i in range(n):
        for j in range(n):
            if std_positions[i][j] == 0:
                empty_.append((i,j))
    return empty_

def find_adjacent(std_positions, cur_y, cur_x, find):
    move = [[-1,0],[1,0],[0,-1],[0,1]]
    found_pos = []
    count = 0
    for m in move:
        if cur_y + m[0] > -1 and cur_y + m[0] < len(std_positions) and cur_x + m[1] > -1 and cur_x + m[1] < len(std_positions):
            if std_positions[cur_y + m[0]][cur_x + m[1]] == find:
                found_pos.append((cur_y + m[0], cur_x + m[1]))
                count += 1
        else:
            continue
    if len(found_pos) == 0:
        return False, [], 0
    else:
        return True, found_pos, count
    
def get_max_likes(empty_seats, std, likes, std_positions):
    max_likes = 0
    max_likes_pos = []
    for seat in empty_seats:
        seat_y, seat_x = seat[0], seat[1]
        num_likes = 0
        for like in likes:
            boolean, pos, count = find_adjacent(std_positions, seat_y, seat_x, like)
            if boolean == True:
                num_likes += 1
        if num_likes > max_likes and num_likes > 0:
            max_likes = num_likes
            max_likes_pos = []
            max_likes_pos.append((seat_y, seat_x))
        elif num_likes == max_likes and num_likes > 0:
            max_likes_pos.append((seat_y, seat_x))
    return max_likes_pos

def get_max_empty(max_likes_pos, std_positions):
    max_empty_count = 0
    max_empty_pos = []
    for seat in max_likes_pos:
        seat_y, seat_x = seat[0], seat[1]
        num_empty = 0
        boolean, pos, count = find_adjacent(std_positions, seat_y, seat_x, 0)
        if boolean == True:
            num_empty = count
            if max_empty_count < count:
                max_empty_count = count
                max_empty_pos = []
                max_empty_pos.append((seat_y,seat_x))
            elif max_empty_count == count:
                max_empty_pos.append((seat_y,seat_x))
    return max_empty_pos

def get_least_number(max_empty_pos):
    return min(max_empty_pos)
    
def assign(std_positions, student_dict):
    for std, likes in student_dict.items():
        #print(f"\nassigning student: {std}")
        empty_seats = get_empty_seats(std_positions)
        max_likes_pos = get_max_likes(empty_seats, std, likes, std_positions)
        if len(max_likes_pos) == 1:
            #print("max likes pos:",max_likes_pos)
            #print("maximum likes (condition 1)")
            assign_y, assign_x = max_likes_pos[0][0],max_likes_pos[0][1]
            std_positions[assign_y][assign_x] = std
            #print_pos(std_positions)
            continue
        elif len(max_likes_pos) == 0:
            max_likes_pos = empty_seats
        max_empty_pos = get_max_empty(max_likes_pos, std_positions)
        if len(max_empty_pos) == 1:
            #print("maximum empty positions (condition 2)")
            assign_y, assign_x = max_empty_pos[0][0], max_empty_pos[0][1]
            std_positions[assign_y][assign_x] = std
            #print_pos(std_positions)
            continue
        elif len(max_empty_pos) == 0:
            max_empty_pos = max_likes_pos
        #print("least number positions (condition 3)")
        least_number_pos = get_least_number(max_empty_pos)
        assign_y, assign_x = least_number_pos[0], least_number_pos[1]
        std_positions[assign_y][assign_x] = std
        #print_pos(std_positions)
    return std_positions

def calculate_sufficiency(std_positions, student_dict):
    n = len(std_positions)
    result_suff = 0
    for i in range(n):
        for j in range(n):
            std = std_positions[i][j]
            likes = student_dict[std]
            seat_y,seat_x = i,j
            n_likes = 0
            for like in likes:
                boolean, pos, count = find_adjacent(std_positions, seat_y, seat_x, like)
                if boolean == True:
                    n_likes +=1
            assert n_likes == 0 or n_likes == 1 or n_likes == 2 or n_likes == 3 or n_likes == 4, print(n_likes)
            if n_likes == 0:
                result_suff += 0
            elif n_likes == 1:
                result_suff += 1
            elif n_likes == 2:
                result_suff += 10
            elif n_likes == 3:
                result_suff += 100
            elif n_likes == 4:
                result_suff += 1000
    return result_suff
'''
### Make test case
for i in range(3,21,1):
    N = i
    print(f"N = {i}")
    student_dict = {}
    for _ in range(N*N):
        likes = random.sample(range(1,N*N),4)
        student_dict[_+1] = likes
    
    std_positions = []
    for u in range(N):
        tmp = []
        for v in range(N):
            tmp.append(0)
        std_positions.append(tmp)
    std_positions = assign(std_positions, student_dict)
    sufficiency = calculate_sufficiency(std_positions, student_dict)
    print(sufficiency)

    
'''
### Get inputs
N = int(input())
student_dict = {}
for i in range(N*N):
    std_ = [int(item) for item in input().split()]
    student_dict[std_[0]] = std_[1:]

### Make matrix of student positions
std_positions = []
for u in range(N):
    tmp = []
    for v in range(N):
        tmp.append(0)
    std_positions.append(tmp)

### Assign students to seats
std_positions = assign(std_positions, student_dict)    

### Calculate sufficiency
sufficiency = calculate_sufficiency(std_positions, student_dict)
print(sufficiency)

