import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        return max(self.maxPathSumTillNode(root))

    def maxPathSumTillNode(self, root):
        if not root:
            return 0, -math.inf

        left_branch, left_max = self.maxPathSumTillNode(root.left)
        right_branch, right_max = self.maxPathSumTillNode(root.right)

        return max(left_branch, right_branch, 0) + root.val, max(left_max, right_max,
                                                                 max(left_branch, 0) + root.val + max(right_branch, 0))
