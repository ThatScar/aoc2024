from collections import Counter

with open("day1.txt") as file:
    locations = [[int(x) for x in line.strip().split("   ")] for line in file]
    left, right = zip(*locations)
    counts_right = Counter(right)
    total = 0
    for i in left:
        total += i*counts_right[i]
    print(total)
