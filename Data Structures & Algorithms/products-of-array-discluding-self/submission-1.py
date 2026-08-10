class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prepopulate info
        leng = len(nums)
        productleft = [1] * leng
        productright = [1] * leng
        for i in range(1, leng, 1):
            productleft[i] = productleft[i-1] * nums[i-1]
            productright[leng - i - 1] = productright[leng - i] * nums[leng - i]
        ans = [0] * leng
        ans[0] = productright[0]
        ans[leng - 1] = productleft[leng - 1]
        for i in range(1,leng - 1,1):
            ans[i] = productleft[i] * productright[i]
        return ans

        

        