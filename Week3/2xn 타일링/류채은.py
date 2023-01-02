ways =[0,1,2]

n = int(input())
idx = 3

for i in range(n-2):
    new_val = ways[idx-2]+ways[idx-1]
    ways.append(new_val)
    idx +=1

print(ways[n]%10007)
