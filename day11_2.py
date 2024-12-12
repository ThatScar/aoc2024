from collections import Counter

with open("day11.txt") as file:
    initial = [int(x) for x in file.read().strip().split()]
print(initial)

##def product(self, other):
##    for key in self.keys():
##        self[key] *= other
##    return self
##Counter.__mul__ = product

counts = Counter(initial)
for _ in range(75):
    new_counts = Counter()
    for stone, count in counts.items():
        if stone == 0:
            new_counts += Counter({1:count})
        else:
            stone_str = str(stone)
            size = len(stone_str)
            if size%2 == 0:
                new_counts += Counter({int(stone_str[:size//2]):count}) + \
                              Counter({int(stone_str[size//2:]):count})
            else:
                new_counts += Counter({stone*2024:count})
    counts = new_counts
print(counts.total())
