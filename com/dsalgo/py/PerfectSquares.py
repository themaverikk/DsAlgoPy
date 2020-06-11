import math


class Solution:

    def numSquares(self, n: int) -> int:
        dp = [0]  # 0,1,2,3

        for i in range(1, n + 1):
            sq_root = math.sqrt(i)

            min_squares = math.inf
            if sq_root.is_integer():
                min_squares = 1
            else:
                for j in range(1, i // 2 + 1):  # j(1,3)
                    min_squares = min(min_squares, dp[j] + dp[i - j])

            dp.append(min_squares)

        return dp[n]


if __name__ == "__main__":
    s = Solution()
    print(s.numSquares(6655))
