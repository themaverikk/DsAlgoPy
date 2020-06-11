import math
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx_prod = -math.inf
        curr_prod = -math.inf
        start = -1
        n = len(nums)

        for i in range(len(nums)):
            if nums[i] == 0:
                mx_prod = max(mx_prod, max(nums[i], curr_prod))

                if start != -1 and curr_prod < 0 and start != (i - 1):
                    begin_prod = 1
                    for j in range(start, i):
                        begin_prod *= nums[j]

                        if nums[j] < 0:
                            break
                    mx_prod = max(mx_prod, curr_prod / begin_prod)

                    end_prod = 1
                    for j in range(i - 1, start - 1, -1):
                        end_prod *= nums[j]

                        if nums[j] < 0:
                            break
                    mx_prod = max(mx_prod, curr_prod / end_prod)
                start = -1

            else:
                if start < 0:
                    curr_prod = nums[i]
                    start = i
                else:
                    curr_prod *= nums[i]

        mx_prod = max(mx_prod, curr_prod)

        if start != -1 and curr_prod < 0 and start != (n - 1):
            begin_prod = 1
            for j in range(start, n):
                begin_prod *= nums[j]

                if nums[j] < 0:
                    break
            mx_prod = max(mx_prod, curr_prod / begin_prod)

            end_prod = 1
            for j in range(n - 1, start - 1, -1):
                end_prod *= nums[j]

                if nums[j] < 0:
                    break
            mx_prod = max(mx_prod, curr_prod / end_prod)

        return int(mx_prod)


if __name__ == "__main__":
    maxProduct = Solution().maxProduct([0, 0, -3, 1])
    print(maxProduct)
