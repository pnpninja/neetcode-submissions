class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        # First get a count of characters
        t_count_map = defaultdict(int)
        for char in t:
            t_count_map[char]+=1
        needed_characters = set(t_count_map.keys())
        remaining_characters = needed_characters.copy()
        
        # Now lets iterate through s
        s_count_map = defaultdict(int)
        l,r = 0,0
        ans = ""
        minLen = 100001
        len_s, len_t = len(s), len(t)
        while r < len_s:
            # if a character is needed, we need to take it
            if s[r] in needed_characters:
                s_count_map[s[r]]+=1
                # once we have enough, we can remove it from remaining
                if s_count_map[s[r]] == t_count_map[s[r]]:
                    remaining_characters.remove(s[r])
            # if we have got all characters we want, try to slide
            # the left side till there is a character we actually need.
            while len(remaining_characters) == 0:
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    ans = s[l:r+1]
                if s[l] in needed_characters:
                    s_count_map[s[l]]-=1
                    if s_count_map[s[l]] < t_count_map[s[l]]:
                        remaining_characters.add(s[l])
                l+=1
            r+=1
        return ans

            

