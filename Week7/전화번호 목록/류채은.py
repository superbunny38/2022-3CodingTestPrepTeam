import sys

def is_consistent(numbers):
    #print("numbers:",numbers)
    for number in list(numbers.keys()):
        for i in range(1,len(number)):
            if number[:i] in numbers:
                return 'NO'
    return 'YES'

answers = []
t = int(sys.stdin.readline().rstrip())
for n_test in range(t):
    n = int(sys.stdin.readline().rstrip())#n phone numbers
    numbers = dict()
    for _ in range(n):
        number = sys.stdin.readline().strip()
        #print("number:",number)
        numbers[number] = 0
    answer = is_consistent(numbers)
    answers.append(answer)

for ans in answers:
    print(ans)
