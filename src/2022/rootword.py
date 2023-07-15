from typing import List
def topKFrequent(nums: List[int], k: int) -> List[int]:
    lookup = {}
    freq = [[] for i in range(len(nums))]
    for i in range(len(nums)):
        lookup[nums[i]] = lookup.get(nums[i], 0) + 1
    print(lookup)
    for num, count in lookup.items():
        freq[count].append(num)
    topk = 0
    out = []
    for i in range(len(freq) - 1, 0, -1):
        for val in freq[i]:
            out.append(val)
            topk += 1
            if topk >= k:
                return out

series=[1,1,1,2,2,3,5]
max_count=2
print(topKFrequent(series, max_count))



"""# Given a sentence with spaces removed "wewanttowatchtheworldcup" and a dictionary (can be all english words / a smaller dictionary) say whether the sentence without spaces can be represented as a sequence of words (repetitions are allowed)

# wewanttowatchtheworldcup -> TRUE
# weatherwewant -> TRUE
# wwanttowatchtheworldcup -> FALSE
# wewanttowatchtheworlcup -> FALSE

# {'we', 'want', ....}

lookup = {
    'we': 0,
    'want': 1,
    'to': 2,
    'watch': 3,
    "the": 4,
    "world": 5,
    "cup": 6,
    "weather": 7
}

def check_remaining_substring(substr:str):
    # 1. we atherwewant
    # 2. weather wewant
    
    #...
    # if  each key matches with the string's prefix, recursively find if the remaning string contains the rest of the keys, 
    # keep a queue to keep track of remaining strings,   
    if len(substr)==0:
        return True 
    valid_flag =False
    for idx in range(len(substr)):
        word = substr[:idx+1]
        # print(word)
        if word in lookup:
            print(word)
            valid_flag = check_remaining_substring(substr[idx+1:])

    return valid_flag 


# # wewanttowatchtheworldcup -> TRUE
# weatherwewant -> TRUE
# wwanttowatchtheworldcup -> FALSE
# wewanttowatchtheworlcup -> FALSE
input_string = "wewanttowatchtheworldcup"
print(check_remaining_substring(input_string))
"""