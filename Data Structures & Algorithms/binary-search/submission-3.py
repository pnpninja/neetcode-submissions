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
            mid = (int)((l + r) / 2)
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid
            else:
                r = mid
        if l == r and nums[l] == target:
            return l
        return -1
            