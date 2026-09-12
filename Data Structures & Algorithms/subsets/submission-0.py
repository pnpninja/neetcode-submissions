class Solution:
    def subsetRecur(self, i: int, nums: List[int], subset: List[int], ans: List[List[int]]) -> None:
        if i == len(nums):
            ans.append(list(subset))
            return
        subset.append(nums[i])
        self.subsetRecur(i + 1, nums, subset, ans)
        subset.pop()
        self.subsetRecur(i + 1, nums, subset, ans)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []
        self.subsetRecur(0, nums, subset, ans)
        return ans