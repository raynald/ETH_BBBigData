#!/usr/bin/python
import sys
import numpy as np

mean_all = [0 for i in range(5)]
var_all = [0 for i in range(5)]
size_all = [0 for i in range(5)]
mean_month = [[0 for i in range(5)] for j in range(12)]
var_month = [[0 for i in range(5)] for j in range(12)]
size_month = [[0 for i in range(5)] for j in range(12)]


codeSet = {'PRCP':0, 'SNOW':1, 'SNWD':2, 'TMAX':3, 'TMIN':4}

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        code, month, num = line.split('\t')
        month = int(month)
        month = month - 1 #let month start from 0
        num = float(num)
        if code in codeSet:
            index = codeSet[code]
            if size_all[index] == 0:
                mean_all[index] = num
                var_all[index] = 0
                size_all[index] = 1
            else:
                var_all[index] = (var_all[index] * size_all[index]) / (size_all[index] + 1) + size_all[index] * ( (mean_all[index] - num) / (size_all[index] + 1))**2
                mean_all[index] = (mean_all[index] * size_all[index] + num) / (size_all[index] + 1)
                size_all[index] = size_all[index] + 1
            if month in range(12):
                if size_month[month][index] == 0:
                    mean_month[month][index] = num
                    var_month[month][index] = 0
                    size_month[month][index] = 1
                else:
                    var_month[month][index] = (var_month[month][index] * size_month[month][index]) / (size_month[month][index] + 1) + size_month[month][index] * ( (mean_month[month][index] - num) / (size_month[month][index] + 1))**2
                    mean_month[month][index] = (mean_month[month][index] * size_month[month][index] + num) / (size_month[month][index] + 1)
                    size_month[month][index] = size_month[month][index] + 1
    for i in range(5):
        print "%d\t%f\t%f" % (i, mean_all[i],var_all[i])

    for i in range(12):
        for j in range(5):
            print "%d\t%d\t%f\t%f" % (i, j, mean_month[i][j],var_month[i][j])
