class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        len_nums = len(nums)
        ans = []
        seen_targets = set()
        for target_ind in range(len_nums - 2):
            target = -sorted_nums[target_ind]
            if target in seen_targets:
                continue
            seen_targets.add(target)
            l, r = target_ind + 1, len_nums - 1
            while l < r:
                if sorted_nums[l] + sorted_nums[r] == target:
                    ans.append([-target, sorted_nums[l], sorted_nums[r]])
                    l+=1
                    while l < len_nums and sorted_nums[l] == sorted_nums[l-1]:
                        l+=1
                    r-=1
                    while r > target_ind and sorted_nums[r] == sorted_nums[r+1]:
                        r-=1
                elif sorted_nums[l] + sorted_nums[r] > target:
                    r-=1
                else:
                    l+=1
        return ans