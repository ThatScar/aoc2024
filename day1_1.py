with open("day1.txt") as file:
    locations = [[int(x) for x in line.strip().split("   ")] for line in file]
    print(locations)
    left, right = zip(*locations)
    left = sorted(left)
    right = sorted(right)
    print(left, right)
    print(sum(right)-sum(left))
    total = 0
    for x, y in zip(left, right):
        total += abs(x-y)
    print(total)
