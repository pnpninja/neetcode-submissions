class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        location = dict()
        for ind in range(len(nums)):
            need = target - nums[ind]
            if need in location:
                return [location[need], ind]
            else:
                location[nums[ind]] = ind
        return []