from typing import List


def is_palindrome(s):
    mid = len(s) // 2
    i, j = 0, len(s) - 1

    while i <= mid <= j:
        if s[i] != s[j]:
            return False

        i += 1
        j -= 1

    return True


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = {}

        return self.palindrome_partition(s, 0, dp)

    def palindrome_partition(self, s, i, dp):
        if i < 0 or i >= len(s):
            return [[]]

        if i in dp:
            return dp[i]

        curr_lists = []
        for j in range(i + 1, len(s) + 1):
            curr_substr = s[i:j]

            if is_palindrome(curr_substr):
                next_palindrome_substrs = self.palindrome_partition(s, j, dp)

                for st in next_palindrome_substrs:
                    curr_list = [curr_substr]
                    curr_list.extend(st)
                    curr_lists.append(curr_list)

        dp[i] = curr_lists

        return dp[i]


if __name__ == "__main__":
    s = Solution()

    print(s.partition("aab"))
