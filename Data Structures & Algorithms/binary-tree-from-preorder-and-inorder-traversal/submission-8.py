# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right

class Worker:
    def __init__(self, preorder, inorder):
        self.preorder = preorder
        self.inorder = inorder
        # Create position map for inorder
        self.map = {}
        for ind, num in enumerate(inorder):
            self.map[num] = ind

    def buildTreeRecur(self, preorderStart: int, preorderEnd: int, inorderStart: int, inorderEnd: int) -> Optional[TreeNode]:
        if preorderStart > preorderEnd or inorderStart > inorderEnd:
            return None
        
        rootVal = self.preorder[preorderStart]
        node = TreeNode(rootVal)
        
        # Find the index of the root in inorder array
        inIndex = self.map[rootVal]
        
        # Number of nodes in the left subtree
        leftSize = inIndex - inorderStart
        
        # Recurse using the calculated sizes to partition preorder and inorder arrays
        node.left = self.buildTreeRecur(preorderStart + 1, preorderStart + leftSize, inorderStart, inIndex - 1)
        node.right = self.buildTreeRecur(preorderStart + leftSize + 1, preorderEnd, inIndex + 1, inorderEnd)
        return node

    def buildTree(self) -> Optional[TreeNode]:
        if len(self.preorder) == 0:
            return None
        return self.buildTreeRecur(0, len(self.preorder) - 1, 0, len(self.inorder) - 1)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        x = Worker(preorder=preorder, inorder=inorder)
        return x.buildTree()

