#주식
#11501

test_cases = []
T = int(input())#n of test cases
for _ in range(T):
    N = int(input())
    stock_prices = input().split()
    stock_prices = [int(x) for x in stock_prices]
    test_cases.append([N]+stock_prices)

for case in test_cases:
    N = case[0]
    stock_prices = case[1:]
    max_ = 0
    total = 0
    for price in stock_prices[::-1]:
        if price>max_:
            max_ = price
        else:#price <= max_
            total -= price
            total += max_
    
    print(total)

