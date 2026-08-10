class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = [0] * 26
        if len(s) != len(t):
            return False
        for pos in range(0,len(s)):
            char_count[ord(s[pos])-97]+=1
            char_count[ord(t[pos])-97]-=1
        for count in char_count:
            if count != 0:
                return False
        return True
