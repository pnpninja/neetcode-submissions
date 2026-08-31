class Solution:
    def partition(self, nums: List[int], l: int, r: int) -> int:
        pivotElem = nums[r]
        pivotInd = l
        for i in range(l,r):
            if nums[i] >= pivotElem:
                nums[i], nums[pivotInd] = nums[pivotInd], nums[i]
                pivotInd+=1
        nums[r], nums[pivotInd] = nums[pivotInd], nums[r]
        return pivotInd

    def findKthLargestInternal(self, nums: List[int], l: int, r: int, k: int) -> int:
        pivot = self.partition(nums, l ,r)
        if pivot - l == k - 1:
            return nums[pivot]
        elif pivot - l > k - 1:
            return self.findKthLargestInternal(nums,l, pivot - 1, k)
        else:
            return self.findKthLargestInternal(nums,pivot + 1, r, k - (pivot - l + 1))
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.findKthLargestInternal(nums,0, len(nums) - 1, k)
