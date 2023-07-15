from typing import List

def kSmallestPairs( nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    p1 = 0
    p2 = 0
    out = []
    for i in range(k):
        out.append([nums1[p1], nums2[p2]])
        print(out)
        if p1 == len(nums1):
            p2 += 1
        elif p2 == len(nums2):
            p1 += 1
        elif nums1[p1] < nums2[p2]:
            p2 += 1
        else:
            p1 += 1
    return out

n1=[1,2]
n2=[3]
nos=3
out=kSmallestPairs(n1, n2, nos)
print(out)