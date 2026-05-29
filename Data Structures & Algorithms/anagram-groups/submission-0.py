class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        
        for s in strs:
            ana = ''.join(sorted(s))
            result[ana].append(s)

        return list(result.values())