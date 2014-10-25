import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

import os.path

def read_feat(dir, dim):
	file_list = listdir(dir)
	num_samp = len(file_list)
	samp_dict = dict()
	data = np.zeros((num_sample, dim))
	for i, file in zip(range(num_samp), file_list):
		data[i,:] = np.genfromtxt(file, delimiter="")
		file_name = path.basename(file)
		samp_name = path.splitext(file_name)[0]
		samp_dict[i] = samp_name
		print samp_name, " processed ", i, "/", num_samp
	return data, samp_dict


def print_cluster(samp_dict, label, filename):
	res_file = open(filename, "w")
	for i in samp_dict:
		text = samp_dict[i] + " " + label[i] + "\n"
		res_file.write(text)
		print i " result printed to file"
	res_file.close()


dim_feat = 120
data_folder = ""
label_file = "./result/cluster.label"
# read feature
data, samp_dict = read_feat(data_folder, dim_feat)
# PCA optional
num_comp = 30
frame = PCA(num_comp, copy=True)
frame.fit(data)
data_PCA = frame.transform(data)
# Kmeans clustering
num_cluster = 30
max_iter = 300
agent = KMeans(num_cluster, max_iter, init="k-means++")
label = agent.fit_predict(data_PCA)
print label.size " samples clustered"
# print label file
print_cluster(samp_dict, label, label_file)
