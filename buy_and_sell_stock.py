from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    # TODO - you fill in here.
    low = prices[0]
    profit = 0
    for i in range(len(prices)):
        if prices[i] - low > profit:
            profit = prices[i] - low
        if prices[i] < low:
            low = prices[i]
    return profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
