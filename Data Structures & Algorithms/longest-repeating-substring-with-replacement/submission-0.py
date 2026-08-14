class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        l, r = 0,0
        max_f = 0
        res = 0
        for r in range(0,len(s),1):
            count[ord(s[r])-65]+=1
            max_f = max(max_f, count[ord(s[r])-65])
            if r - l + 1 - max_f > k:
                count[ord(s[l])-65]-=1
                l+=1
            res = max(res, r - l + 1)
        return res
            

        