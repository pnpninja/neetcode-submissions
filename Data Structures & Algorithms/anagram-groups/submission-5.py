class Solution:
    def signWord(self, word: str) -> str:
        count = [0] * 26
        for char in word:
            count[ord(char)-97]+=1
        sign = ""
        for i in range(0,26):
            sign+=chr(i+97)
            sign+=str(count[i])
        return sign
    def groupWords(self, strs: List[str]) -> dict[str, List[str]]:
        word_dict = defaultdict(list)
        for word in strs:
            signed_word = self.signWord(word)
            word_dict[signed_word].append(word)
        return word_dict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = self.groupWords(strs)
        return list(word_dict.values())
        