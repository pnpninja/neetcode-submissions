class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_nos = set()
        for num in nums:
            if num in seen_nos:
                return True
            seen_nos.add(num)
        return False
        