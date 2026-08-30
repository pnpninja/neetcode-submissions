# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBSTRecur(self, root: Optional[TreeNode], low: int, high: int) -> bool:
        if not root:
            return True
        if root.val >= high or root.val <= low:
            return False
        return self.isValidBSTRecur(root.left, low, root.val) and self.isValidBSTRecur(root.right, root.val, high)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTRecur(root, -1000000001, 1000000001)