class Solution:
    def trap_stack(self, height: List[int]) -> int:
        ans, stack = 0, list()
        cur, leng = 0, len(height)
        while cur < leng:
            while len(stack) != 0 and height[cur] > height[stack[-1]]:
                top = stack[-1]
                stack.pop()
                if len(stack) == 0:
                    break
                distance = cur - stack[-1] - 1
                bounded_height = min(height[cur], height[stack[-1]]) - height[top]
                ans += distance * bounded_height
            stack.append(cur)
            cur += 1
        return ans
    def trap(self, height: List[int]) -> int:
        return self.trap_stack(height)
