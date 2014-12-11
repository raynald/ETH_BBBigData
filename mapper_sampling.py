#!/usr/bin/python
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
        if int(year)!=2013:# or int(year)!=2003 or int(year)!=1993 or int(year)!=1983:
            continue
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
    #sample_ratio = 0.5
    sample_ratio = 1
    #retain_ratio = 0.5
    retain_ratio = 1
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
        # monitoring progress
        sys.stderr.write(str(num_pt_retained) + " / "\
            + str(num_pt_coreset) + " sampled\n")

    # assign membership
    # dist_all = euclidean_distances(data, data[list(coreset),:])
    # membership1 = np.argmin(dist_all, axis=-1)

    core_list = list(coreset)
    block_size = 1000.0
    membership_list = []
    for i in range(int(ceil(num_pt/block_size))):
        pt_start = i * int(block_size)
        pt_end = (i + 1) * int(block_size)
        dist_list = []
        for j in range(int(ceil(num_pt_coreset/block_size))):
            core_start = j * int(block_size)
            core_end = (j + 1) * int(block_size)
            dist_list.append(euclidean_distances(
                data[pt_start:pt_end, :], data[core_list[core_start:core_end], :]))
        dist = np.hstack(dist_list)
        membership_list.append(np.argmin(dist, axis=-1) )
    membership = np.hstack(membership_list)

    # assert np.all(membership1 == membership)

    member_cnt = []
    for i in range(len(coreset)):
        member_cnt.append((membership == i).sum())

    # sanity check
    assert len(coreset) == num_pt_coreset
    assert sum(member_cnt) == num_pt

    # output coreset to reducer
    for i, pt in enumerate(list(coreset)):
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

