# Python3 implementation of the approach

# Function to return the maximum profit
# that can be made after buying and
# selling the given stocks
def maxProfit(price):
    if not price or len(price) < 2:
        return 0

    profit = 0
    buyPrice = price[0]
    bought = False

    for i in range(1, len(price)):
        if price[i] > price[i - 1]:
            if not bought:
                bought = True
                buyPrice = price[i - 1]

            if i == len(price) - 1:
                bought = False
                profit += (price[i] - buyPrice)

        elif price[i] < price[i - 1]:
            if bought:
                bought = False
                profit += (price[i - 1] - buyPrice)

    return profit


# Driver code
if __name__ == '__main__':
    price = [100, 180, 260, 310, 40, 535, 695];
    n = len(price);

    print(maxProfit(price));

# This code is contributed by Rajput-Ji
