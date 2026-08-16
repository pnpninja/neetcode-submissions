class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_map = defaultdict(int)
        for ch in t:
            count_map[ch] = count_map.get(ch, 0) + 1
        characters_needed = set(count_map.keys())
        curr_count_map = defaultdict(int)
        l, r = 0, 0
        len_s = len(s)
        min_len = math.inf
        ans = ""
        while r < len_s:
            if s[r] not in count_map:
                r+=1
            else:
                curr_count_map[s[r]] = curr_count_map.get(s[r], 0) + 1
                if curr_count_map[s[r]] >= count_map[s[r]]:
                    characters_needed.discard(s[r])
                r+=1
                # found all characters
                if len(characters_needed) == 0:
                    while len(characters_needed) == 0:
                        if s[l] not in count_map:
                            l+=1
                        else:
                            curr_count_map[s[l]] = curr_count_map.get(s[l], 0) - 1
                            if curr_count_map[s[l]] < count_map[s[l]]:
                                characters_needed.add(s[l])
                                if r - l + 1 < min_len:
                                    min_len = r - l + 1
                                    ans = s[l:r]
                            l+=1
        return ans

