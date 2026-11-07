class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            elif nums[l] <= nums[mid]:
                if nums[l] <= target and target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid
        if nums[l] == target:
            return l
        return -1
            