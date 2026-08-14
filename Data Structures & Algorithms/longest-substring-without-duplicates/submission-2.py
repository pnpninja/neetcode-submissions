class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        char_loc = [-1] * 256
        cur_len, max_len = 1, 1
        left_ptr, right_ptr = 0, 1
        s_len = len(s)
        char_loc[ord(s[left_ptr])] = left_ptr
        while left_ptr <= right_ptr and right_ptr < s_len:
            # new character not seen
            if char_loc[ord(s[right_ptr])] == -1:
                cur_len+=1
                char_loc[ord(s[right_ptr])] = right_ptr
                right_ptr+=1
            # new character was seen. So move left_ptr to just next of 
            else:
                old_loc, new_loc = char_loc[ord(s[right_ptr])], right_ptr
                while left_ptr <= old_loc:
                    char_loc[ord(s[left_ptr])] = -1
                    left_ptr+=1
                    cur_len-=1
                char_loc[ord(s[right_ptr])] = right_ptr
                cur_len = right_ptr - left_ptr + 1
                right_ptr+=1
            max_len = max(max_len, cur_len)
        return max_len


