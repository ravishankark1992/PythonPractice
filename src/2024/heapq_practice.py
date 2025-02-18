def frequent_elements(nums):
    import heapq
    from collections import Counter
    freq = Counter(nums)
    priority = []
    for k,v in freq.items():

        heapq.heappush(freq, (v,k))

frequent_elements(nums=[1,1,1,2,3,3])