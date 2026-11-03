class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count, s2_count = [0] * 26, [0] * 26
        remaining_characters = set()
        needed_characters = set()
        for char in s1:
            s1_count[ord(char)-97]+=1
            remaining_characters.add(char)
            needed_characters.add(char)
        l, r = 0, 0
        while r < len(s2):
            if s2[r] in needed_characters:
                s2_count[ord(s2[r])-97]+=1
                if s2_count[ord(s2[r])-97] == s1_count[ord(s2[r])-97]:
                    remaining_characters.remove(s2[r])
            if r - l + 1 > len(s1):
                if s2[l] in needed_characters:
                    s2_count[ord(s2[l])-97]-=1
                    if s2_count[ord(s2[l])-97] < s1_count[ord(s2[l])-97]:
                        remaining_characters.add(s2[l])
                l+=1
            r+=1
            if len(remaining_characters) == 0:
                return True
        return False


        
        
