def max_profit(prices, k):
    n = len(prices)
    profit = [[0 for _ in range(k + 1)] for _ in range(n)]

    min_price = prices[0]
    for i in range(1, n):
        min_price = min(min_price, prices[i])

        for j in range(1, k + 1):
            profit[i][j] = max(profit[i - 1][j], profit[i - 1][j - 1] + prices[i] - min_price)

    return profit[n - 1][k]


if __name__ == '__main__':
    k = 2
    prices = [10, 22, 5, 75, 65, 80]

    print("Maximum profit is:", max_profit(prices, k))
