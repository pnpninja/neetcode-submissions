class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        curLen, maxLen = 0, 0
        for num in nums:
            if num - 1 in numSet:
                continue
            iter = num
            curLen = 0
            while iter in numSet:
                curLen+=1
                iter+=1
            maxLen = max(maxLen, curLen)
        return maxLen