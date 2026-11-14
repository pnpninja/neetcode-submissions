class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans, stack = 0, []
        for ind, height in enumerate(heights):
            start = ind
            while stack and stack[-1][0] > height:
                prev_height, prev_start = stack.pop()
                ans = max(ans, prev_height * (ind - prev_start))
                start = prev_start
            stack.append((height, start))

        for height,start in stack:
            ans = max(ans, height * (len(heights) - start))
        return ans