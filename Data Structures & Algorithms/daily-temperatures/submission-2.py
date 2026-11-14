class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack of temperature and index
        stack = []
        len_temperatures = len(temperatures)
        ans = [0] * len_temperatures
        for i in range(len_temperatures - 1, -1, -1):
            if i == len_temperatures - 1:
                stack.append((temperatures[i], i))
            else:
                while stack and stack[-1][0] <= temperatures[i]:
                    stack.pop()
                if stack:
                    ans[i] = stack[-1][1] - i
                else:
                    ans[i] = 0
                stack.append((temperatures[i], i))
        return ans