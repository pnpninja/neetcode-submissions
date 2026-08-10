from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def countChars(stri: str) -> List:
            count = [0] * 26
            for c in stri:
                count[ord(c)-97]+=1
            return count
        def createSignature(arr: List[int]) -> str:
            finalStr = ""
            for i in range(0, 26):
                finalStr+=chr(i+97)
                finalStr+=str(arr[i])
            return finalStr
        mapg = defaultdict(list)
        for stri in strs:
            count = countChars(stri)
            signature = createSignature(count)
            mapg[signature].append(stri)
        ans = []
        for key,val in mapg.items():
            ans.append(val)
        return ans