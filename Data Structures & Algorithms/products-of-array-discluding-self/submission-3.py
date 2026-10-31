class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftCumProduct, rightCumProduct = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)):
            leftCumProduct[i] = nums[i-1] * leftCumProduct[i-1]
        for i in range(len(nums) - 2, -1, -1):
            rightCumProduct[i] = nums[i+1] * rightCumProduct[i+1]
        ans = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                ans[i] = rightCumProduct[i]
            elif i == len(nums) - 1:
                ans[i] = leftCumProduct[i]
            else:
                ans[i] = rightCumProduct[i] * leftCumProduct[i]
        return ans