class Solution:
    def recur(self, nums: List[int], target: int, index: int, current: List[int], ans: Set[List[int]]):
        if target == 0:
            sortedAns = tuple(sorted(current))
            if sortedAns not in ans:
                ans.add(sortedAns)
            return
        if index == len(nums):
            return
        if target < 0:
            return
        current.append(nums[index])
        self.recur(nums, target-nums[index], index + 1, current, ans)
        current.pop()
        while index + 1 < len(nums) and nums[index + 1] == nums[index]:
            index += 1
        self.recur(nums, target, index + 1, current, ans)
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = set()
        current = []
        self.recur(candidates, target, 0, current, ans)
        realAns = [list(x) for x in ans]
        return realAns