class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        r1 = Counter(ransomNote)
        m1 = Counter(magazine)
        # soln: return r1&m1==r1
        for c in ransomNote:
            if c not in m1:
                return False
            else:
                print(r1)
                r1[c]=r1[c]-1
                m1[c]=m1[c]-1
                if r1[c]==0:
                    del r1[c]
                if m1[c]==0:
                    del m1[c]
        print(r1)
        if len(r1)==0:
            return True
        return False

x=Solution()
y=x.canConstruct('aa', 'aab')
print(y)