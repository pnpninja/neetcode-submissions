class Solution:
    def recur(self, nums: List[int], idx: int, ans = List[List[int]]) -> None:
        if idx == len(nums):
            ans.append(nums[:])
            return
        for i in range(idx, len(nums)):
            nums[i], nums[idx] = nums[idx], nums[i]
            self.recur(nums, idx + 1, ans)
            nums[i], nums[idx] = nums[idx], nums[i]

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.recur(nums, 0, ans)
        return ans