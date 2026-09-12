class Solution:
    def recur(self, nums: List[int], target: int, index: int, current: List[int], ans: List[List[int]]):
        if target == 0:
            ans.append(list(current))
            return
        if index == len(nums):
            return
        if target < 0:
            return
        current.append(nums[index])
        self.recur(nums, target-nums[index], index, current, ans)
        #self.recur(nums, target-nums[index], index + 1, current, ans)
        current.pop()
        self.recur(nums, target, index + 1, current, ans)
        
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        current = []
        self.recur(nums, target, 0, current, ans)
        return ans