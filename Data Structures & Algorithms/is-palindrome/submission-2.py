class Solution:
    def isPalindrome(self, s: str) -> bool:
        leng = len(s)
        leftPtr, rightPtr = 0, leng - 1
        while leftPtr < rightPtr:
            while not s[leftPtr].isalnum() and leftPtr < rightPtr:
                leftPtr+=1
            while not s[rightPtr].isalnum() and leftPtr < rightPtr:
                rightPtr-=1
            if leftPtr > rightPtr:
                return True
            if s[leftPtr].lower() != s[rightPtr].lower():
                return False
            else:
                leftPtr+=1
                rightPtr-=1
        return True