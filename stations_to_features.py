#!/usr/bin/python

import sys
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale


codeSet = {'PRCP':0, 'SNOW':1, 'SNWD':2, 'TMAX':3, 'TMIN':4}

feature = np.array([])
year_feature = np.array([])
data = np.array([])
samp_dict = dict()
count = 0
old_key = ""
old_year = ""
old_month = ""

def print_cluster(samp_dict, label, file_name):
    for i in samp_dict:
        print "%s\t%s\t%d" % (file_name, samp_dict[i], label[i])


if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        year, key, month, code, num = line.split('\t')
        if old_key == "":
            old_key = key
            old_year = year
            old_month = month
        if code in codeSet:
            if year == old_year:
                if key == old_key:
                    if month == old_month:
                        feature = np.append(feature, [int(num)])
                    else:
                        year_feature = np.append(year_feature, feature.mean(), feature.var())
                        feature = np.array([int(num)])
                        old_month = month
                else:
                    if feature.size > 0:
                        year_feature = np.append(year_feature, feature.mean(), feature.var())
                        feature = np.array([])
                    if count == 0:
                        data = year_feature
                    else:
                        data = np.append(data, year_feature, axis=1)
                    samp_dict[count] = old_key
                    key = old_key
                    count += 1
            else:
                if year_feature.size > 0:
                    data = np.append(data, year_feature, axis=1)
                    year_feature = np.array([])
                if data.size > 0:
                    data = scale(data, copy=True)
                    # PCA optional
                    num_comp = 30
                    frame = PCA(num_comp, copy=True)
                    frame.fit(data)
                    data_PCA = frame.transform(data)
                    # Kmeans clustering
                    num_cluster = 100
                    num_iter = 300
                    agent = KMeans(num_cluster, init="k-means++", \
                           max_iter=num_iter, precompute_distances=True)
                    label = agent.fit_predict(data_PCA)
                    # print label file
                    print_cluster(samp_dict, label, old_year)
                    samp_dict = dict()
                    feature = np.array([])
                    data = np.array([])
                    count = 0
                    old_year = year
    if year_feature.size > 0:
        data = np.append(data, year_feature, axis=1)
        year_feature = np.array([])
    if data.size > 0:
        data = scale(data, copy=True)
        # PCA optional
        num_comp = 30
        frame = PCA(num_comp, copy=True)
        frame.fit(data)
        data_PCA = frame.transform(data)
        # Kmeans clustering
        num_cluster = 100
        num_iter = 300
        agent = KMeans(num_cluster, init="k-means++", \
               max_iter=num_iter, precompute_distances=True)
        label = agent.fit_predict(data_PCA)
        # print label file
        print_cluster(samp_dict, label, old_year)
        samp_dict = dict()
        feature = np.array([])
        data = np.array([])
        count = 0
        old_year = year
        

