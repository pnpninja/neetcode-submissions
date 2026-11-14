# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maxD = 0
    
    def recurse(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        maxLeft = self.recurse(root.left)
        maxRight = self.recurse(root.right)
        curDepth = max(maxLeft, maxRight) + 1
        self.maxD = max(self.maxD, curDepth)
        return curDepth

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maxD = 0
        return self.recurse(root)