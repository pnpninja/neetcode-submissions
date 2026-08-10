class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arrays = defaultdict(list) # sets list as default for any nonexistent value
        for s in strs:
            ss = "".join(sorted(s))
            arrays[ss].append(s)
        return list(arrays.values())