class Solution:
    def recur(self, nums: List[int], idx: int, candidate: List[int], ans: List[List[int]]) -> None:
        if idx == len(nums):
            ans.append(candidate[:])
            return
        candidate.append(nums[idx])
        self.recur(nums, idx + 1, candidate, ans)
        candidate.pop()
        while idx + 1 < len(nums) and nums[idx + 1] == nums[idx]:
            idx+=1
        self.recur(nums, idx + 1, candidate, ans)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        self.recur(nums, 0 , [], ans)
        return ans 