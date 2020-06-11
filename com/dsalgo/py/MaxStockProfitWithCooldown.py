from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = [0] * (n + 2)

        for i in range(n):
            profit_till_now = 0

            for j in range(i):
                profit_till_now = max(profit_till_now, prices[i] - prices[j] + profit[j])

            profit_till_now = max(profit_till_now, profit[i + 1])

            profit[i + 2] = profit_till_now

        return profit[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([]))
