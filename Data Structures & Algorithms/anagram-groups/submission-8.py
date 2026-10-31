class Solution:
    def calculateHash(self, word: str) -> str:
        count = [0]*26
        for char in word:
            count[ord(char)-97]+=1
        return ",".join([str(num) for num in count])

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for word in strs:
            hashMap[self.calculateHash(word)].append(word)
        ans = []
        for _, value in hashMap.items():
            ans.append(value)
        return ans
