#15989
#류채은

numbers = []

T = int(input())#n of test cases
for _ in range(T):
    n = int(input())
    numbers.append(n)
    
memoization = [0 for _ in range(max(numbers))]
memoization = [1] + memoization

for i in range(1,4):
    for j in range(len(memoization)):
        if j>= i:
            memoization[j] += memoization[j-i]

for num in numbers:
    print(memoization[num])
