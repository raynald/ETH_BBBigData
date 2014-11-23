import numpy as np
import sys
import random
import time
from sklearn.metrics.pairwise import euclidean_distances

if __name__ == "__main__":
    # hard coded centroid
    # centroid = np.array([1,3,4,5,6,76,8])
    centroid = np.array([[],[]])

    # read data
    info_list = []
    data = []
    for line in sys.stdin:
    # line  = "s1\t1990\t1,3,4,5,6,76,8"
        station, year, feature = line.split("\t")
        info_list.append((station, year))
        data.append(np.fromstring(feature, dtype=np.double, sep=','))
    data = np.array(data)
    num_data = data.shape[0]

    dist_all = euclidean_distances(data, centroid)
    membership = np.argmin(dist_all, axis=-1)

    # output to reducer
    assert len(membership) == num_data
    for i in range(num_data):
        data_str = info_list[i][0] + "\t" + info_list[i][1]\
             + "\t" + str(membership[i])
        print data_str
