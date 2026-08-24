# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maxDiameter = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxLeft = self.maxDepth(root.left)
        maxRight = self.maxDepth(root.right)
        self.maxDiameter = max(self.maxDiameter, maxLeft + maxRight)
        return 1 + max(maxLeft, maxRight)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0
        self.maxDepth(root)
        return self.maxDiameter