class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                height, index = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append([h, start])

        for h,i in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area