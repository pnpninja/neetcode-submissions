class Solution:
    def isPalindrome(self, s: str) -> bool:
        len_s = len(s)
        left, right = 0, len_s - 1
        while left < right:
            while left < len_s and not s[left].isalnum():
                left+=1
            while right > 0 and not s[right].isalnum():
                right-=1
            if left > right:
                break
            if s[left].lower() != s[right].lower():
                return False
            left+=1
            right-=1
        return True