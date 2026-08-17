# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def maxDepthHelper(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depthLeft = self.maxDepthHelper(root.left)
        depthRight = self.maxDepthHelper(root.right)
        return 1 + max(depthLeft, depthRight)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.maxDepthHelper(root)