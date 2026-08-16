class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for ind, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, prev_ind = stack.pop()
                ans[prev_ind] = ind - prev_ind
            stack.append((temp, ind))
        return ans
