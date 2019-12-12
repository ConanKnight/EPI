from test_framework import generic_test


def buy_and_sell_stock_twice(prices):
    # TODO - you fill in here.
    # return 0.0
    # max_profit = 0
    # lowest = prices[0]
    # max_profit_arr = [0]*len(prices)
    # for i in range(len(prices)):
    #     # if prices[i] - lowest > max_profit:
    #     max_profit = max(max_profit, prices[i] - lowest)
    #     # if prices[i] < lowest:
    #     lowest = min(lowest, prices[i])
    #     max_profit_arr[i] = max_profit
    # # print(max_profit_arr)
    # # reversed_prices = reversed(prices)
    # max_profit_arr.insert(0, 0)
    # max_profit2 = 0
    # max_profit_arr2 = [0]*len(prices)
    # largest_sell = prices[-1]
    # for i in reversed(range(len(prices))):
    #     # if prices[i] > largest_sell:
    #     largest_sell = max(largest_sell, prices[i])
    #     # if largest_sell - prices[i] > max_profit2:
    #     max_profit2 = max(max_profit2, largest_sell - prices[i])
    #     max_profit_arr2[i] = max_profit2
    # for i in range(len(prices)):
    #     max_profit_arr[i] += max_profit_arr2[i]
    # return max(max_profit_arr)

    # Generalized Method
    T20, T10 = 0, 0
    T21, T11 = float('-inf'), float('-inf')

    for price in prices:
        T20 = max(T20, T21 + price)
        T21 = max(T21, T10 - price)
        T10 = max(T10, T11 + price)
        T11 = max(T11, -price)
    return T20


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock_twice.py",
                                       "buy_and_sell_stock_twice.tsv",
                                       buy_and_sell_stock_twice))
