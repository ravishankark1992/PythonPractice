class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_space = 0
        while s[-1]==' ':
            s=s[:-1]
        while s[0]==' ':
            s=s[1:]
        print(s)
        for i in range(len(s)):
            if s[i]==" ":
                last_space=i
        if last_space==0:
            return len(s)
        return len(s)-last_space-1