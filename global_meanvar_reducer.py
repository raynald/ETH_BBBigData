#!/usr/bin/python
import sys
import numpy as np

mean_all = [0 for i in range(5)]
var_all = [0 for i in range(5)]
size_all = [0 for i in range(5)]

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        code, mean, var, size = line.split('\t')
        code = int(code)
        mean = float(mean)
        var = float(var)
        size = int(size)
        if code in range(5):
            print "yes"
            if size_all[code] == 0:
                mean_all[code] = mean
                var_all[code] = var
                size_all[code] = size
            elif size > 0:
                var_all[code] = (var_all[code] * size_all[code] + var * size) / (size_all[code] + size) + (size_all[code] * size) * ( (mean_all[code] - mean) / (size_all[code] + size))**2
                mean_all[code] = (mean_all[code] * size_all[code] + mean * size) / (size_all[code] + size)
                size_all[code] = size_all[code] + size
    for i in range(5):
        print "%d\t%f\t%f" % (i, mean_all[i],var_all[i])
