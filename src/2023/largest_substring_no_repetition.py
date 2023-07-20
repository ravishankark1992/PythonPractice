class LargestSubstring:
    def find_largest_substring(self, text):
        longest = 0
        history = {}
        for i, c in enumerate(text):
            if c in history:
                last_seen = history[c]
        return

text = "abcabcbb"
text = "pwwekw"
query = LargestSubstring()
out = query.find_largest_substring(text)
print(out)
