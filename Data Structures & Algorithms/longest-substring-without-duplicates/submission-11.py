from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        lastPosition = defaultdict(int)
        l, r = 0, 1
        curLen, maxLen = 1, 1
        lastPosition[s[0]] = 0
        for r in range(1, len(s), 1):
            if s[r] in lastPosition:
                # Duplicate found.
                # Slide left pointer to r
                # Clear the entries
                oldPos = lastPosition[s[r]]
                while l <= oldPos:
                    del lastPosition[s[l]]
                    l+=1
                    curLen-=1
            curLen+=1
            maxLen = max(maxLen, curLen)
            lastPosition[s[r]] = r
        return maxLen