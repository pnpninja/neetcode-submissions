# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maxSum = -math.inf
    def maxPathSumRecur(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxSumLeft = 0 if not root.left else max(0, self.maxPathSumRecur(root.left))
        maxSumRight = 0 if not root.right else max(0, self.maxPathSumRecur(root.right))
        self.maxSum = max(self.maxSum, root.val + maxSumLeft + maxSumRight)
        return root.val + max(maxSumLeft, maxSumRight)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root.left == None and root.right == None:
            return root.val
        self.maxSum = -math.inf
        self.maxPathSumRecur(root)
        return int(self.maxSum)
