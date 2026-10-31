class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        ans = []
        if s == "":
            return []
        arr = s.split("#",maxsplit=1)
        l = int(arr[0])
        if l == len(arr[1]):
            return [arr[1]]
        else:
            ans.append(arr[1][0:l])
            recur = self.decode(arr[1][l:])
            return ans + recur
            
