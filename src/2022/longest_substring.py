def lengthOfLongestSubstring(s: str) -> int:
    lookup = {}
    current_length = 0
    longest = 0
    current_substring_start = 0
    for i, letter in enumerate(s):

        if letter in lookup and lookup[letter] >= current_substring_start:
            current_substring_start = lookup[letter] + 1
            current_length = i - lookup[letter]
            lookup[letter] = i
        else:
            lookup[letter] = i
            current_length += 1
            if current_length > longest:
                longest = current_length
    return longest


input_string = "abcdefabax"
print(lengthOfLongestSubstring(input_string))
