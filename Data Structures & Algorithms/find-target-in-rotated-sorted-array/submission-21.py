class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            if l + 1 == r:
                if nums[l] == target:
                    return l
                elif nums[r] == target:
                    return r
                return -1
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                if target >= nums[mid] and target <= nums[r]:
                    l = mid
                else:
                    r = mid
            else:
                if target >= nums[l] and target <= nums[mid]:
                    r = mid
                else:
                    l = mid
        if l == r and nums[l] == target:
            return l
        return -1