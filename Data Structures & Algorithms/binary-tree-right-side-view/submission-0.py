# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maxHeight = -1
    def traverse(self, root: TreeNode, lvl: int, map: dict):
        if not root:
            return
        if lvl not in map:
            map[lvl] = root.val
            self.maxHeight = lvl
        self.traverse(root.right, lvl + 1, map)
        self.traverse(root.left, lvl + 1, map)
        
        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        map = defaultdict(int)
        self.maxHeight = -1
        self.traverse(root, lvl=0, map=map)
        ans = []
        for idx in range(0, self.maxHeight+1,1):
            ans.append(map[idx])
        return ans

        
        
        

