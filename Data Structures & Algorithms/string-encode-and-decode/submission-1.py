class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for st in strs:
            encoded_str+=str(len(st))
            encoded_str+="#"
            encoded_str+=st
        return encoded_str
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        leng = 0
        ptr = 0
        while s[ptr] != '#':
            leng = (leng*10) + int(s[ptr])
            ptr+=1
        ans = list()
        ans.append(s[ptr+1:ptr+1+leng])
        if ptr+1+leng == len(s):
            return ans
        ans+=(self.decode(s[ptr+1+leng:]))
        return ans
