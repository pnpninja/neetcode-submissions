# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, root: Optional[TreeNode], level: int, map: defaultdict[int, list[int]]) -> int:
        if root is None:
            return 0
        map[level].append(root.val)
        l, r = self.traverse(root.left, level + 1, map), self.traverse(root.right, level + 1, map)
        return max(l, r) + 1

        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        map = defaultdict(list[int])
        maxLevel = self.traverse(root, 0, map)
        ans = []
        for i in range(0, maxLevel):
            ans.append(map[i])
        return ans