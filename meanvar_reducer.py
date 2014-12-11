#!/usr/bin/python
import sys
import numpy as np

mean_all = np.zeros(5)
var_all = np.zeros(5)
size_all = np.zeros(5)
codeSet = {'PRCP':0, 'SNOW':1, 'SNWD':2, 'TMAX':3, 'TMIN':4}
ind = 0

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        station_id, year, month, code, num = line.split('\t')
        nummer = float(num)
        if code in codeSet:
            ind = codeSet[code]
            size_all[ind] += 1
            new_mean = (mean_all[ind] * (size_all[ind]-1) + nummer)/size_all[ind]
            var_all[ind] = ((var_all[ind]+mean_all[ind]*mean_all[ind])*(size_all[ind]-1)+nummer*nummer) / size_all[ind] - new_mean * new_mean;
            mean_all[ind] = new_mean
    for i in range(5):
        print "%d\t%f\t%f\t%d" % (i, mean_all[i],var_all[i], size_all[i])
