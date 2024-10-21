from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        dp = [[0]*rows]*rows
        for j in range(rows-1, -1, -1):
            # j -> levels
            for i in range(j+1):
                
                if j<rows-1:
                    #print(j,i)
                    dp[j][i] = min(dp[j][i]+dp[j+1][i+1], dp[j][i]+dp[j+1][i])
                    #print(dp)
                else:
                    dp[j][i] = triangle[j][i]
                    print(dp)
            #print(dp)
        #print(dp)
        return dp[0][0]
x=Solution()
out = x.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
print(out)