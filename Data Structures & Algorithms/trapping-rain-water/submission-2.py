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
    def trap_ptrs(self, height: List[int]) -> int:
        left_ptr, right_ptr = 0, len(height) - 1
        left_max, right_max = 0, 0
        ans = 0
        while left_ptr < right_ptr:
            if height[left_ptr] < height[right_ptr]:
                left_max = max(left_max, height[left_ptr])
                ans+=left_max - height[left_ptr]
                left_ptr+=1
            else:
                right_max = max(right_max, height[right_ptr])
                ans+=right_max - height[right_ptr]
                right_ptr-=1
        return ans
    def trap(self, height: List[int]) -> int:
        return self.trap_ptrs(height)
