# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recurse(self, root: Optional[TreeNode], level: int, seen : set, ans: list[int]) -> None:
        if not root:
            return
        if level not in seen:
            ans.append(root.val)
            seen.add(level)
        self.recurse(root.right, level + 1, seen, ans)
        self.recurse(root.left, level + 1, seen, ans)

        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        seen = set()
        ans = []
        self.recurse(root, 0, seen, ans)
        return ans