class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        if len(s2) == len(s1) and s1 == s2:
            return True
        original_count_map = {}
        for c in s1:
            original_count_map[c] = original_count_map.get(c, 0) + 1
        curr_count_map = {}
        remaining_letters = set(original_count_map.keys())
        l, r = 0, 0
        len_s1, len_s2 = len(s1), len(s2)
        while r < len_s2:
            if s2[r] in original_count_map:
                curr_count_map[s2[r]] = curr_count_map.get(s2[r], 0) + 1
                if curr_count_map[s2[r]] == original_count_map[s2[r]]:
                    remaining_letters.remove(s2[r])
            if r - l + 1 > len_s1:
                # analyze the beginning character
                if s2[l] in original_count_map:
                    curr_count_map[s2[l]] = curr_count_map[s2[l]] - 1
                    if curr_count_map[s2[l]] < original_count_map[s2[l]]:
                        remaining_letters.add(s2[l])
                l += 1
            r += 1
            # print(s2[l:r])
            # print(remaining_letters)
            if len(remaining_letters) == 0:
                return True
        if len(remaining_letters) == 0:
            return True
        return False
