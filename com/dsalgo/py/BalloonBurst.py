from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        balloons = [1] + [x for x in nums if x > 0] + [1]
        dp = [[0 for _ in range(len(balloons))] for _ in range(len(balloons))]

        return self.maxCoinsBurst(balloons, 1, len(balloons) - 2, dp)

    def maxCoinsBurst(self, balloons, l, r, dp):  # 1,5,8,1, l=1, r=2, k=1
        if l < 0 or l >= len(balloons) or r < 0 or r >= len(balloons) or r < l:
            return 0

        if dp[l][r] > 0:
            return dp[l][r]

        max_coins = 0
        for k in range(l, r + 1):
            coins = self.maxCoinsBurst(balloons, l, k - 1, dp) + self.maxCoinsBurst(balloons, k + 1, r, dp) \
                    + balloons[l - 1] * balloons[k] * balloons[r + 1]

            max_coins = max(max_coins, coins)

        dp[l][r] = max_coins
        return dp[l][r]


if __name__ == "__main__":
    s = Solution()
    print(s.maxCoins([3, 1, 5, 8]))
