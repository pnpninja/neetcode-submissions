class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = []
        for ind in range(len(height)):
            while len(stack) > 0 and height[ind] > height[stack[-1]]:
                top = stack.pop()
                if len(stack) == 0:
                    break
                width = ind - stack[-1] - 1
                bounded_height = min(height[ind], height[stack[-1]]) - height[top]
                ans+=width*bounded_height
            stack.append(ind)
        return ans


