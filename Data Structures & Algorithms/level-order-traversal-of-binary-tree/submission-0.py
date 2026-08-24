# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans, curLevel = [], []
        curLevel.append(root)
        while len(curLevel) != 0:
            nextLevel = []
            levelAnswers = []
            for node in curLevel:
                if not node:
                    continue
                levelAnswers.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            if len(levelAnswers) != 0:
                ans.append(levelAnswers)
            curLevel = nextLevel
        return ans
        