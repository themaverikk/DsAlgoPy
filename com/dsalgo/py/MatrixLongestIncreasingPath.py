from typing import List


def is_valid(matrix, i, j):
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        longest_path = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                curr_longest_path = self.currLongestIncreasingPath(matrix, i, j, dp)
                longest_path = max(longest_path, curr_longest_path)

        return longest_path

    def currLongestIncreasingPath(self, matrix, i, j, dp):
        if not is_valid(matrix, i, j):
            return 0

        if dp[i][j]:
            return dp[i][j]

        x = [-1, 1, 0, 0]
        y = [0, 0, -1, 1]

        next_longest_path = 0
        for idx in range(len(x)):
            next_x = i + x[idx]
            next_y = j + y[idx]
            if is_valid(matrix, next_x, next_y) and matrix[next_x][next_y] > matrix[i][j]:
                next_longest_path = max(next_longest_path,
                                        self.currLongestIncreasingPath(matrix, next_x, next_y, dp))

        dp[i][j] = 1 + next_longest_path

        return dp[i][j]


if __name__ == "__main__":
    s = Solution()

    nums = [[1, 2]]

    print(s.longestIncreasingPath(nums))
