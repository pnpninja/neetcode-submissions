# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maxDiameter = 0
    
    def recurse(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        maxLeft, maxRight = self.recurse(root.left), self.recurse(root.right)
        diameter = maxLeft + maxRight
        self.maxDiameter = max(self.maxDiameter, diameter)
        return 1 + max(maxLeft, maxRight)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0
        self.recurse(root)
        return self.maxDiameter