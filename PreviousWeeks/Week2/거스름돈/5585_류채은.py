#거스름돈
#5585

def n_change(payment):
    payment = 1000-payment
    answer =0
    units = [500,100,50,10,5,1]
    for unit in units:
        n_unit = payment//unit
        #print(f"${unit}: {n_unit}장")
        answer += n_unit
        payment -= n_unit*unit
    return answer

payment = int(input())
print(n_change(payment))
