from typing import List
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        out = [[0]*n]*m
        print(out)
        for i in range(m):
            for j in range(n):
                
                #print(n*i+j, original[(n*i)+j])
                out[i][j] = original[(n*i)+j]
                print(out)
        return out

# Test the function
original = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
m = 3
n = 4
solution = Solution()
solution.construct2DArray(original, m, n)