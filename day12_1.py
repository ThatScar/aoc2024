region = []
with open("day12.txt") as file:
    for line in file:
        line = line.strip()
        region.append(list(line))

def print_region(region):
    for line in region:
        print("".join(line))

VISITED = "."
total = 0
for i, line in enumerate(region):
    for j, crop in enumerate(line):
        if crop == VISITED:
            continue

        size = 0
        perimeter = 0
        splore = [(i,j)]
        while splore and (pos:=splore.pop()):
            y, x = pos
            if region[y][x] == VISITED:
                continue
            else:
                region[y][x] = VISITED
            size += 1
            perimeter += 4
            for y, x in [(y-1,x),(y,x-1),(y,x+1),(y+1,x)]:
                if y<0 or len(region)<=y or x<0 or len(region[0])<=x:
                    continue
                if region[y][x] == crop:
                    perimeter -= 2
                    splore.append((y,x))
        print(crop, size, perimeter)
        total += size*perimeter
print(total)
