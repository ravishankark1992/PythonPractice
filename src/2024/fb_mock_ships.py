class Solution:
    def shipWithinDays(self, weights, days: int) -> int:
        l = max(weights)
        r = res = sum(weights)

        def canShip(cap, weights):
            ships, curr_cap = 1, cap
            for w in weights:
                if curr_cap - w < 0:
                    ships+=1
                    curr_cap = cap
                curr_cap = curr_cap - w
            return ships <= days
                

        while l<=r:
            cap = (l+r)//2
            if canShip(cap, weights):
                res = min(res, cap)
                r = cap-1
            else:
                l=cap+1
        return res
    
o=Solution()
print(o.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))