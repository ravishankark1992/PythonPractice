from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = {}
        for word in strs:
            new = sorted(word)
            new="".join(new)
            if new in lookup:
                lookup[new].append(word)
            else:
                lookup[new] = [word]
        return lookup


x=Solution()
x.groupAnagrams(["eat","tea","tan","ate","nat","bat"])