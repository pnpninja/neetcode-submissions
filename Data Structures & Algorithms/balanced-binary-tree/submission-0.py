# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepthAndBalanced(self, root: Optional[TreeNode]) -> tuple[int, bool]:
        if not root:
            return 0, True
        left_depth, left_balanced = self.maxDepthAndBalanced(root.left)
        right_depth, right_balanced = self.maxDepthAndBalanced(root.right)
        balanced = left_balanced and right_balanced
        if balanced and abs(left_depth - right_depth) > 1:
            balanced = False
        return (max(left_depth, right_depth) + 1, balanced)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        _, balanced = self.maxDepthAndBalanced(root)
        return balanced