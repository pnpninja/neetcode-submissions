class Solution:
    def recur(self, nums: List[int], target: int, start: int, current: List[int], ans: List[List[int]]):
        if target == 0:
            ans.append(current[:])
            return
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue  # skip duplicates at this recursion level
            if nums[i] > target:
                break  # sorted, so nothing further can work either
            current.append(nums[i])
            self.recur(nums, target - nums[i], i + 1, current, ans)
            current.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        current = []
        self.recur(candidates, target, 0, current, ans)
        return ans