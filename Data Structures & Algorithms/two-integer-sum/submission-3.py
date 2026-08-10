class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        posMap = dict()
        for i in range(0,len(nums)):
            diff = target - nums[i]
            if diff in posMap:
                return [posMap[diff], i]
            posMap[nums[i]] = i
        return [-1,-1]
        