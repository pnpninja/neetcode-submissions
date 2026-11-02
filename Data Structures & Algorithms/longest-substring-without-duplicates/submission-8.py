from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        lastPosition = defaultdict(int)
        l, r = 0, 1
        curLen, maxLen = 1, 1
        lastPosition[s[0]] = 0
        while r < len(s):
            if s[r] not in lastPosition:
                curLen+=1
                maxLen = max(maxLen, curLen)
                lastPosition[s[r]] = r
                r+=1
            else:
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
                r+=1
        return maxLen