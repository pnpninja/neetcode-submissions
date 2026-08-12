class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        leftPtr, rightPtr = 0, len(heights) - 1
        while leftPtr < rightPtr:
            curVol = (rightPtr - leftPtr) * min(heights[leftPtr], heights[rightPtr])
            if curVol > ans:
                ans = curVol

            if heights[leftPtr] < heights[rightPtr]:
                leftPtr+=1
            else:
                rightPtr-=1
        return ans
            