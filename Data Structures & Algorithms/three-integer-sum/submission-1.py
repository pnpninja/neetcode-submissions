class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = list()
        for ind in range(0, len(nums) - 2, 1):
            if ind > 0 and nums[ind] == nums[ind - 1]:
                continue
            target = -nums[ind]
            leftPtr, rightPtr = ind + 1, len(nums) - 1
            while leftPtr < rightPtr:
                if nums[leftPtr] + nums[rightPtr] == target:
                    ans.append([nums[ind], nums[leftPtr], nums[rightPtr]])
                    leftPtr+=1
                    while nums[leftPtr-1] == nums[leftPtr] and leftPtr < rightPtr:
                        leftPtr+=1
                    rightPtr-=1
                    while nums[rightPtr+1] == nums[rightPtr] and rightPtr > leftPtr:
                        rightPtr-=1
                elif nums[leftPtr] + nums[rightPtr] > target:
                    rightPtr-=1
                    while nums[rightPtr+1] == nums[rightPtr] and rightPtr > leftPtr:
                        rightPtr-=1
                else:
                    leftPtr+=1
                    while nums[leftPtr-1] == nums[leftPtr] and leftPtr < len(nums):
                        leftPtr+=1
        return ans
                    