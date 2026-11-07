class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        if len(nums1) == 0 and len(nums2) == 0:
            return 0
        if len(nums1) == 0:
            if len(nums2)%2:
                return nums2[len(nums2)//2]
            return (nums2[len(nums2)//2 - 1] + nums2[len(nums2)//2]) / 2
        if len(nums2) == 0:
            if len(nums1)%2:
                return nums1[len(nums1)//2]
            return (nums1[len(nums1)//2 - 1] + nums1[len(nums1)//2]) / 2
        total = len(nums1) + len(nums2)
        half = total // 2
        l, r = 0, len(nums1)

        while True:
            nums1_mid = (l + r) // 2
            nums2_mid = half - nums1_mid - 2

            nums1_left = nums1[nums1_mid] if nums1_mid >= 0 else float("-infinity")
            nums1_right = nums1[nums1_mid + 1] if nums1_mid + 1 < len(nums1) else float("infinity")
            nums2_left = nums2[nums2_mid] if nums2_mid >= 0 else float("-infinity")
            nums2_right = nums2[nums2_mid + 1] if nums2_mid + 1 < len(nums2) else float("infinity")

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                return (
                    min(nums1_right, nums2_right)
                    if total % 2
                    else (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
                )
            if nums1_left > nums2_right:
                r = nums1_mid - 1
            else:
                l = nums1_mid + 1
