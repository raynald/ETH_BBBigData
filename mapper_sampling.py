import numpy as np
import sys
import random
import time
from sklearn.metrics.pairwise import euclidean_distances
from math import floor, ceil

if __name__ == "__main__":
    # read data
    info_list = []
    data = []
    for line in sys.stdin:
    # line  = "s1\t1990\t1,3,4,5,6,76,8"
        station, year, feature = line.split("\t")
        info_list.append((station, year))
        data.append(np.fromstring(feature, dtype=np.double, sep=','))
    data = np.array(data)

    # # generate test data
    # info_list = []
    # num_data = 10
    # data = np.zeros((num_data, 15))
    # for i in range(num_data/2):
    #     data[i * 2, i * 3] = 1
    #     data[i * 2, i * 3 + 1] = 1
    #     data[i * 2 + 1, i * 3 + 1] = 1
    #     data[i * 2 + 1, i * 3 + 2] = 1
    #     info_list.append((2 * i, 2 * i))
    #     info_list.append((2 * i + 1, 2 * i + 1))


    # parameters
    num_pt = data.shape[0]
    sample_ratio = 0.06
    retain_ratio = 0.5
    num_pt_coreset = ceil(num_pt * retain_ratio)

    # generate core set with uniform sampling
    pt_set = set(range(num_pt))
    num_pt_retained = 0
    coreset = [] 
    while num_pt_retained < num_pt_coreset:
        # uniformly sample pts to be added to core set
        num_sample = int(min(ceil(num_pt * sample_ratio),\
                             num_pt_coreset - num_pt_retained))
        sample = random.sample(pt_set, num_sample)
        coreset += sample
        num_pt_retained += len(sample)
        # find first half of nearest points and remove
        # guarantee enough pt for next round    
        num_pt_remove = min( (len(pt_set) - len(sample))\
                            - (num_pt_coreset - num_pt_retained),
                            ceil( (len(pt_set) - len(sample)) / 2))  
        dist_all = euclidean_distances(data[list(pt_set), :], data[sample, :])
        dist = np.amin(dist_all, axis=-1)  
        pt_id_sort = dist.argsort()
        # remove uniformly selected samples and first half of nearest pts
        pt_list = list(pt_set)
        for pt in pt_id_sort[0:(num_pt_remove+num_sample)]:
            pt_set.remove(pt_list[pt])

    # assign membership
    dist_all = euclidean_distances(data, data[coreset,:])
    membership = np.argmin(dist_all, axis=-1)
    member_cnt = []
    for i in range(len(coreset)):
        member_cnt.append((membership == i).sum())

    # sanity check
    assert len(coreset) == num_pt_coreset
    assert sum(member_cnt) == num_pt

    # output coreset to reducer
    for i, pt in enumerate(coreset):
        data_str = "%f" % data[pt, 0]
        data_str += "".join([",%f" % value for value in data[pt,1:]])
        print "%s\t%d" % (data_str, member_cnt[i])

    # # output test
    # for pt in coreset:
    #     print pt, " cen ", data[pt, :]
    # for i in range(num_data):
    #     # assert euclidean_distances(data[i,:], data[coreset[membership[i]], :]) < 2
    #     print membership[i], " memeber ", data[i,:], "\n", data[coreset[membership[i]], :]
    # print member_cnt
        








