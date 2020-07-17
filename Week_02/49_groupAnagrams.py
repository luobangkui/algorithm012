class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash =  {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in hash:
                hash[key].append(s)
            else:
                hash[key] = [s]
        return list(hash.values())