import numpy
from collections import Counter

total_safe = 0
with open("day2.txt") as file:
    for line in file:
        report = numpy.array([int(x) for x in line.strip().split(" ")])
        report_diff = numpy.diff(report)
        if (all( 1 <= report_diff) and all(report_diff <=  3)) or \
           (all(-3 <= report_diff) and all(report_diff <= -1)):
            total_safe += 1
print(total_safe)
