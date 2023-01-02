#파이썬 스터디
#1,2,3 더하기
#9095번
#류채은

def sum_three(n):
    if n > 2:
        return sum_three(n-3) + sum_three(n-2) + sum_three(n-1)
    elif n == 0:
        return 1
    elif n == 1:
        return 2
    elif n == 2:
        return 4

times = int(input())
ans = []
for i in range(times):
    n = int(input())
    ans.append(sum_three(n-1))

for value in ans:
    print(value)
    
