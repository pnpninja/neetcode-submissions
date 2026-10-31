class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftCumProduct, rightCumProduct = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)):
            leftCumProduct[i] = nums[i-1] * leftCumProduct[i-1]
            rightCumProduct[len(nums)-1-i] = nums[len(nums)-1-i+1] * rightCumProduct[len(nums)-1-i+1]            
        ans = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                ans[i] = rightCumProduct[i]
            elif i == len(nums) - 1:
                ans[i] = leftCumProduct[i]
            else:
                ans[i] = rightCumProduct[i] * leftCumProduct[i]
        return ans