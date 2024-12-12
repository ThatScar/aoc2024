from functools import cache

topography = []
with open("day10.txt") as file:
    for line in file:
        topography.append(line.strip())

@cache
def get_peaks(y,x, expected_height) -> int:
    if y<0 or len(topography[0])<=y or \
       x<0 or len(topography)   <=x or \
       int(topography[y][x]) != expected_height:
        return 0
    elif expected_height == 9:
        return 1
    else:
        h = expected_height + 1
        return get_peaks(y-1,x,h) + get_peaks(y,x-1,h) + \
               get_peaks(y,x+1,h) + get_peaks(y+1,x,h)

total = 0
for i, line in enumerate(topography):
    for j, tile in enumerate(line):
        if int(tile) == 0:
            total += get_peaks(i,j, 0)
print(total)
