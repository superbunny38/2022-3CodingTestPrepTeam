#2331
#류채은
A,P = map(int, input().split())
sunyeol = [A]
#print(A)
arr = list(str(A))

while True:
    num = 0
    for each in arr:
        num += int(each)**P
    #print(num)
    if num not in sunyeol:
        sunyeol.append(num)
        arr = list(str(num))
    else:
        where = sunyeol.index(num)
        print(where)
        break
        
    
