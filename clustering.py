import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import cPickle as pickle

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

from os import listdir
from os import path

def read_feat(dir, dim):
	file_list = listdir(dir)
	num_samp = len(file_list)
	samp_dict = dict()
	data = np.zeros((num_samp, dim))
	for i, file_name in zip(range(num_samp), file_list): 
		# remove the nan at the last position
		data[i,:] = np.genfromtxt(dir + file_name, delimiter=",")[0:-1]
		file_name = path.basename(file_name)
		samp_name = path.splitext(file_name)[0]
		samp_dict[i] = samp_name
		print samp_name, " processed ", i, "/", num_samp
	return data, samp_dict


def print_cluster(samp_dict, label, filename):
	res_file = open(filename, "w")
	for i in samp_dict:
		text = samp_dict[i] + " " + str(label[i]) + "\n"
		res_file.write(text)
		print i, " result printed to file"
	res_file.close()


dim_feat = 60
data_folder = "./features/"
label_file = "./result/cluster.label"
# read feature
# data, samp_dict = read_feat(data_folder, dim_feat)
# with open("./data_feat.txt", 'w') as data_file:
# 	pickle.dump(data, data_file)
# with open("./dict.txt", 'w') as dict_file:
# 	pickle.dump(samp_dict, dict_file)

with open("./data_feat.txt", 'r') as data_file:
	pickle.load(data_file)
with open("./dict.txt", 'r') as dict_file:
	pickle.load(dict_file)


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
print label.size, " samples clustered"
# print label file
print_cluster(samp_dict, label, label_file)
