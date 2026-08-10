class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in range(0,len(s)):
            count[ord(s[i])-97] = count[ord(s[i])-97] + 1
            count[ord(t[i])-97] = count[ord(t[i])-97] - 1
        for i in range(0,26):
            if count[i] != 0:
                return False
        return True