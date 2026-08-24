# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.count = 0
    
    def traverse(self, root: TreeNode, maxValInPath: int) -> None:
        if not root:
            return
        if root.val >= maxValInPath:
            self.count+=1
        maxValInPath = max(maxValInPath, root.val)
        self.traverse(root.left, maxValInPath)
        self.traverse(root.right, maxValInPath)
        
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        maxValInPath = -101
        self.traverse(root, maxValInPath)
        return self.count
