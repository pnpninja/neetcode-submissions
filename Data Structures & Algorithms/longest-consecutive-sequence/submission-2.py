class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0
        for num in numSet:
            if num-1 in numSet:
                continue
            curLen = 1
            nextNum = num+1
            while nextNum in numSet:
                curLen+=1
                nextNum+=1
            maxLen = max(curLen, maxLen)
        return maxLen
