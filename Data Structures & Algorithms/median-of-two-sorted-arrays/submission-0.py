class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        l, r = 0, len(nums1) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2
            nums1_left = nums1[i] if i >= 0 else float("-infinity")
            nums1_right = nums1[i + 1] if i < len(nums1) - 1 else float("infinity")
            nums2_left = nums2[j] if j >= 0 else float("-infinity")
            nums2_right = nums2[j + 1] if j < len(nums2) - 1 else float("infinity")
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if total % 2 == 1:
                    return min(nums1_right, nums2_right)
                else:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            elif nums1_left > nums2_right:
                r = i - 1
            else:
                l = i + 1