from collections import Counter

days = ["Mon", "Tue", "Wed", "Thu"]
counter = Counter(days)
print(counter)
for x in range(1, 5, 2):
    d = x % 3
    counter.update([days[d]] * x)
print(counter)
