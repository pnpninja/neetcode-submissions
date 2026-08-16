class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = [[p,s] for p, s in zip(position, speed)]
        pairs = sorted(pairs, key = lambda x: (-x[0], x[1]))
        for _, pair in enumerate(pairs):
            t = (target - pair[0])/pair[1]
            stack.append(t)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)