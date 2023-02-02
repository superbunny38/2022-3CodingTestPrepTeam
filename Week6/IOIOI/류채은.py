

N = int(input())
S = int(input())#string length
pool = input()
assert S == len(pool)

length = 2*N+1
#print("find:",find)
count = 0
idx = 0
found = 0

while True:
    if idx+3>S:
        break
    if pool[idx:idx+3] == "IOI":
        idx+=2
        found +=1
        if found == N:
            found-=1
            count+=1
    else:
        idx+=1
        found=0
    
print(count)
