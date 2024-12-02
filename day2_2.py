import numpy
from collections import Counter

total_safe = 0
with open("day2.txt") as file:
    for line in file:
        report = numpy.array([int(x) for x in line.strip().split(" ")])
        for i in range(len(report)):
            dampened_report = numpy.concatenate((report[:i], report[i+1:]))
            ## identity at i == len(report)
            report_diff = numpy.diff(dampened_report)
            if (all( 1 <= report_diff) and all(report_diff <=  3)) or \
               (all(-3 <= report_diff) and all(report_diff <= -1)):
                total_safe += 1
                break
print(total_safe)
