class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Get counts
        count_map = defaultdict(int)
        for num in nums:
            count_map.setdefault(num,0)
            count_map[num]+=1
        count_arr = [[] for _ in range(len(nums) + 1)]
        for num, count in count_map.items():
            count_arr[count].append(num)
        ans = []
        ctr = 0
        limit_reached = False
        count_arr.reverse()
        for nums in count_arr:
            if not nums:
                continue
            for num in nums:
                ans.append(num)
                ctr+=1
                if ctr == k:
                    limit_reached = True
                    break
            if limit_reached:
                break
        return ans

        