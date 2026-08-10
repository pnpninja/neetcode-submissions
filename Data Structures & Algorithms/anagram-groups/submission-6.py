class Solution:
    def signWord(self, word: str) -> List(int):
        count = [0] * 26
        for char in word:
            count[ord(char)-97]+=1
        return count
    def groupWords(self, strs: List[str]) -> dict[str, List[str]]:
        word_dict = defaultdict(list)
        for word in strs:
            word_dict[tuple(self.signWord(word))].append(word)
        return word_dict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = self.groupWords(strs)
        return list(word_dict.values())
        