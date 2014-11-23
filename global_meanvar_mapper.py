#!/usr/bin/python
import sys
import re
import numpy as np

codeSet = {'PRCP':0, 'SNOW':1, 'SNWD':2, 'TMAX':3, 'TMIN':4}
feature = []
feature += [np.array([])]
feature += [np.array([])]
feature += [np.array([])]
feature += [np.array([])]
feature += [np.array([])]
def main(argv):
    line = sys.stdin.readline() 
    t = 0
    try:
        while line:
            t += 1
            if t % 100000 == 0:
                print t
            #station_id = line[0:11]
            #year = line[12:16]
            #month = line[16:18]
            #day = line[18:20] 
            code = line[21:25]
            num = line[26:].split(',')[0]
            if code in codeSet:
                feature[codeSet[code]] = np.append(feature[codeSet[code]], [int(num)])
            line = sys.stdin.readline()
        for i in range(5):
            if feature[i].size > 0:
                print "%d\t%f\t%f\t%d" % (i, feature[i].mean(), feature[i].var(), feature[i].size)
            else:
                print "%d\t%f\t%f\t%d" % (i, 0, 0, feature[i].size)
    except "end of file":
        return None

if __name__ == "__main__":
    main(sys.argv)
