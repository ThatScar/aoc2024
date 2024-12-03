import re

total = 0
do = True
with open("day3.txt") as file:
    for match in re.finditer("mul\((\d+),(\d+)\)|do\(\)|don't\(\)", file.read()):
        #print(match.group())
        if match.group()[:4] == "do()":
            do = True
        if match.group()[:7] == "don't()":
            do = False
        if match.group()[:3] == "mul" and do:
            total += int(match.group(1))*int(match.group(2))
print(total)
