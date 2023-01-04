#11399
#ATM

n = int(input())

time = list(map(int, input().split()))

time.sort()
#print(time)
result = 0

i = 1
while i <= n:
    j = 0
    while j < i:
        #print(time[j],'+',end='')
        result = result + time[j]
        j = j + 1
    i = i + 1
    #print("\n")

print(result)
    
