import re

total = 0
with open("day3.txt") as file:
    for match in re.finditer("mul\((\d+),(\d+)\)", file.read()):
        #print(match.group())
        total += int(match.group(1))*int(match.group(2))
print(total)
