import sys
import numpy as np

codeSet = {'PRCP':0, 'SNOW':1, 'SNWD':2, 'TMAX':3, 'TMIN':4}

feature = np.array([])
old_key = ""
old_year = ""
old_month = ""

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        key, date, code, num = line.split('\t')
        year = date[0:4]
        month = date[4:6]
        day = date[6:8]
        if code in codeSet:
            if key == old_key and year == old_year and month == old_month:
                feature = np.append(feature, [int(num)])
            else:
                print "%s\t%s\t%s\t%f\t%f" % (old_key, old_year, old_month, feature.mean(), feature.var())
                old_key = key
                old_year = year
                old_month = month
                feature = np.array([int(num)])

