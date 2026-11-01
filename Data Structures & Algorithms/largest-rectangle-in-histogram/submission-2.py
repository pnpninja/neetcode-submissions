class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []
        for ind in range(len(heights)):
            start = ind
            while len(stack) > 0 and stack[-1][0] > heights[ind]:
                prev_height, prev_start = stack.pop()
                ans = max(ans, prev_height * (ind - prev_start))
                start = prev_start
            stack.append([heights[ind], start])

        for prev_height, prev_start in stack:
            ans = max(ans, prev_height * (len(heights) - prev_start))
        return ans