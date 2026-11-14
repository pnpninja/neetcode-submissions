class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        infos, l = [], len(speed)
        for i in range(0, l):
            infos.append((position[i], speed[i]))
        infos = sorted(infos, key=lambda x: (-x[0], x[1]))
        stack = []
        for p, s in infos:
            t = (target - p)/s
            stack.append(t)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
