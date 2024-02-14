def buy_and_sell(inp):
    sell = max(inp)
    buy = min(inp)

    if inp.index(buy) < inp.index(sell):
        profit = sell - buy
    else:
        profit = 0
    return profit

print(buy_and_sell([8, 10, 7, 5, 7, 15]))  # Maximum Profit: 10
print(buy_and_sell([1, 2, 8, 1]))           # Maximum Profit: 7
print(buy_and_sell([9,8,7,6,5,4,3,2,1]))
