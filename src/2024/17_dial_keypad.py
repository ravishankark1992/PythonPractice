from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "":
            return []
        result=[]
        lookup = {
            "2" : "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        sol = [] # this will contain a list of characters
        n=len(digits)
        
        def recursive(i=0):
            if i == n:
                result.append("".join(sol[:]))
                return
            text = digits[i]
            for c in lookup[text]:
                sol.append(c)
                recursive(i+1)
                sol.pop()

        recursive(0)
        return result


ob = Solution()
print(ob.letterCombinations("234"))