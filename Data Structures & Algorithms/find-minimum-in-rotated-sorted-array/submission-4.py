class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            if l+1 == r:
                return min(nums[l], nums[r])
            mid = (l + r) // 2
            if nums[l] <= nums[mid]:
                if nums[mid] <= nums[r]:
                    r = mid
                else:
                    l = mid
            else:
                if nums[mid] <= nums[r]:
                    r = mid
                else:
                    l = mid
        return nums[r]

