#피보나치 수 2
#2748

def fibo(n):
    save = [0,1]
    for _ in range(n-1):
        second_last = save[-2]
        last = save[-1]
        save.append(second_last+last)
    #print(save)
    return save[-1]
    

n = int(input())
print(fibo(n))
