region = []
with open("day12.txt") as file:
    for line in file:
        line = line.strip()
        region.append(list(line))

def print_region(region):
    for line in region:
        print("".join(line))

# lower means visited
total = 0
for i, line in enumerate(region):
    for j, crop in enumerate(line):
        if crop.islower():
            continue

        size = 0
        sides = 0
        splore = [(i,j)]
        while splore and (pos:=splore.pop()):
            y, x = pos
            if region[y][x].islower():
                continue
            else:
                region[y][x] = region[y][x].lower()
            size += 1
            sides += 4
            for y2, x2 in [(y-1,x),(y,x-1),(y,x+1),(y+1,x)]:
                if y2<0 or len(region)<=y2 or x2<0 or len(region[0])<=x2:
                    continue
                if region[y2][x2] == crop:
                    sides -= 2
                    splore.append((y2,x2))
                if region[y2][x2].lower() == crop.lower():
                    dy = y2-y
                    dx = x2-x
                    y3, x3 = y -dx, x +dy
                    y4, x4 = y2-dx, x2+dy
                    if y4<0 or len(region)<=y4 or x4<0 or len(region[0])<=x4 or \
                       (region[y3][x3].lower() != crop.lower() and \
                        region[y4][x4].lower() != crop.lower()):
                        sides -= 1
        print(crop, size, sides)
        total += size*sides
print(total)
