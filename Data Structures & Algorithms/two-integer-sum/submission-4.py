class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        loc_map = dict()
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in loc_map:
                return [loc_map[diff], i]
            loc_map[nums[i]] = i
        return [-1, -1]