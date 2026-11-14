# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recurse(self, root: Optional[TreeNode]) -> tuple[bool, int]:
        if root is None:
            return True, 0
        leftBalance, leftMax = self.recurse(root.left)
        rightBalance, rightMax = self.recurse(root.right)
        if not leftBalance or not rightBalance or abs(leftMax - rightMax) > 1:
            return False, 0
        return True, max(leftMax, rightMax) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.recurse(root)[0]