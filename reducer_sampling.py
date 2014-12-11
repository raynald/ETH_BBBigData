#!/usr/bin/python
import numpy as np
import sys
import time

from sklearn.cluster import KMeans

if __name__ == "__main__":
    data = []
    weight = []
    for line in sys.stdin:
    # line  = "1,3,4,5,6,76,8\t5"
        feature, member_cnt = line.split("\t")
        data.append(np.fromstring(feature, dtype=np.double, sep=','))
        weight.append(int(member_cnt))
    data = np.array(data)
    print data.shape
    dim = data.shape[1]
    weight = np.array(weight, dtype=np.double)
    weight = np.ones(len(weight))#, dtype=np.double)

    # run weighted kmeans clustering
    num_cluster = 75
    #num_cluster = 300
    num_iter = 300
    # initialize weight kmeans with non-weighted kmeans results
    num_iter_init = 100

    # # generate test data
    # info_list = []
    # num_data = 10
    # dim = 15
    # data = np.zeros((num_data, 15))
    # for i in range(num_data/2):
    #     data[i * 2, i * 3] = 1
    #     data[i * 2, i * 3 + 1] = 1
    #     data[i * 2 + 1, i * 3 + 1] = 1
    #     data[i * 2 + 1, i * 3 + 2] = 1
    #     info_list.append((2 * i, 2 * i))
    #     info_list.append((2 * i + 1, 2 * i + 1))

    # num_cluster = 5
    # num_iter_init = 100
    # num_iter = 100
    # weight = np.ones(num_data)

    start = time.clock()
    agent = KMeans(num_cluster, init="k-means++",\
                   max_iter=num_iter_init, precompute_distances=True)
    agent.fit(data)
    for i in range(num_iter):
        membership = agent.predict(data)
        for i in range(num_cluster):
            # the return is a tuple, we need to use [0]
            member_id = np.where(membership == i)[0]
            weight_member = weight[member_id]
            weight_member = weight_member / weight_member.sum()
            weight_member = np.tile(weight_member, [dim, 1]).transpose()
            data_member = data[member_id, :]
            agent.cluster_centers_[i, :] = \
                np.sum(weight_member * data_member, axis=0)
    finish = time.clock()
    sys.stderr.write(str(data.shape[0]) + " is clustered in " + str(finish -start) + "s\n")

    # output the centroid to file
    for i in range(num_cluster):
        centroid = agent.cluster_centers_[i,:]
        data_str = "%f" % centroid[0]
        data_str += "".join([",%f" % value for value in centroid[1:]])
        print data_str

    # # test output
    # membership = agent.predict(data)
    # for i in range(num_cluster):
    #     print "center ", i, agent.cluster_centers_[i, :]
    # for i in range(num_data):
    #     print "mem ", membership[i], " ", data[i, :]



