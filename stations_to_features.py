#!/usr/bin/python
import sys
import numpy as np

codeSet = {'PRCP':0, 'SNOW':1, 'SNWD':2, 'TMAX':3, 'TMIN':4}
feature = []
feature += [np.array([])]
feature += [np.array([])]
feature += [np.array([])]
feature += [np.array([])]
feature += [np.array([])]
old_key = ""
old_year = ""
old_month = ""

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        key, year, month, code, num = line.split('\t')
        if code in codeSet:
            if key == old_key and year == old_year and month == old_month:
                feature[codeSet[code]] = np.append(feature[codeSet[code]], [int(num)])
            else:
                for i in range(5):
                    if feature[i].size > 0:
                        print "%s\t%s\t%s\t%f\t%f" % (old_key, old_year, old_month, feature[i].mean(), feature[i].var())
                        feature[i] = np.array([])
                old_key = key
                old_year = year
                old_month = month
                feature[codeSet[code]] = np.append(feature[codeSet[code]], [int(num)])
    for i in range(5):
        if feature[i].size > 0:
            print "%s\t%s\t%s\t%f\t%f" % (old_key, old_year, old_month, feature[i].mean(), feature[i].var())
