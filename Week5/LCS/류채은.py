from collections import deque
#틀림

def LCS(list_string1, list_string2):
    
    answer = 0
    queue1,queue2 = deque(),deque()
    
    for letter1, letter2 in zip(list_string1, list_string2):
        n_queue1,n_queue2 = len(queue1),len(queue2)
        print("\nletter1:",letter1,"letter2:",letter2)
        print("queue1:",queue1)
        print("queue2:",queue2)
        if n_queue2 == 0:
            queue1.append(letter1)
        else:
            if letter1 in queue2:
                while True:
                    popped = queue2.popleft()
                    if popped == letter1:
                        break
                print("answer++:",letter1)
                answer+=1
            else:
                queue1.append(letter1)
        if n_queue1 == 0:
            queue2.append(letter2)
        else:
            if letter2 in queue1:
                while True:
                    popped = queue1.popleft()
                    if popped == letter2:
                        break
                answer+=1
                print("answer++:",letter2)
            else:
                queue2.append(letter2)
        
    return answer

string1 = list(input())
string2 = list(input())

print(LCS(string1,string2))
