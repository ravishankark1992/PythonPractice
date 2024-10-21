from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        out = []
        intervals = sorted(intervals, key=lambda x: x[0])
        for i in range(len(intervals)):
            if len(out)>0 and out[-1][1]>=intervals[i][0]:
                # overlap
                out[-1][1]=max(intervals[i][1], out[-1][1])
            else:
                out.append(intervals[i])
        return out
    
# [[1,3],[2,6],[8,10],[15,18]]