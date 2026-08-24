# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getPath(self, root: TreeNode, target: TreeNode, path: List[TreeNode]) -> bool:
        if not root:
            return False
        if root == target:
            path.append(root)
            return True
        else:
            path.append(root)
            if self.getPath(root.left, target, path):
                return True
            elif self.getPath(root.right, target, path):
                return True
            else:
                path.pop()
                return False
             
        
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pPath = []
        self.getPath(root, p, pPath)
        qPath = []
        self.getPath(root, q, qPath)

        leng = min(len(pPath), len(qPath))
        for idx in range(0, leng):
            if pPath[idx] == qPath[idx]:
                continue
            else:
                return pPath[idx - 1]
        return pPath[leng - 1]