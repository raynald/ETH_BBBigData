import sys
import os
import numpy

if __name__ == "__main__":
	filelist = os.listdir('./stations')
	features_means_values = [dict({'PRCP':[], 'SNOW':[], 'SNWD':[], 'TMAX':[], 'TMIN':[]}) for i in range(15)]
	features_variances_values = [dict({'PRCP':[], 'SNOW':[], 'SNWD':[], 'TMAX':[], 'TMIN':[]}) for i in range(15)]
	features_means = [dict({'PRCP':0, 'SNOW':0, 'SNWD':0, 'TMAX':0, 'TMIN':0}) for i in range(15)]
	features_variances = [dict({'PRCP':0, 'SNOW':0, 'SNWD':0, 'TMAX':0, 'TMIN':0}) for i in range(15)]
	count = 0
	for station_id in filelist: # calculate features
		if station_id[0] == '.': #system files
			continue
		count += 1
		if count % 1000 == 0:
			print count
		path = './stations/' + station_id
		f = open(path, "r")
		file_features_counts= [dict({'PRCP':0, 'SNOW':0, 'SNWD':0, 'TMAX':0, 'TMIN':0}) for i in range(15)]
		file_features_values = [dict({'PRCP':[], 'SNOW':[], 'SNWD':[], 'TMAX':[], 'TMIN':[]}) for i in range(15)]
		file_features_means = [dict({'PRCP':0, 'SNOW':0, 'SNWD':0, 'TMAX':0, 'TMIN':0}) for i in range(15)]
		file_features_variances = [dict({'PRCP':0, 'SNOW':0, 'SNWD':0, 'TMAX':0, 'TMIN':0}) for i in range(15)]
		required_codes = {'PRCP', 'SNOW', 'SNWD', 'TMAX', 'TMIN'}
		for line in f:		
			line = line.strip()
			year = int(line[0:4])
			month = int(line[4:6])
			day = int(line[6:8])
			code = line[9:13]
			num = int(line[14:])
			if code not in required_codes:
				continue
			file_features_values[month][code].append(num)
			file_features_counts[month][code] = file_features_counts[month][code]  + 1
		for i in range(1,13):
			for j in required_codes:
				if file_features_counts[i][j] > 0:
					file_features_means[i][j] = numpy.mean(file_features_values[i][j])
					features_means_values[i][j].append(file_features_means[i][j])
					file_features_variances[i][j] = numpy.var(file_features_values[i][j])
					#file_features_variances[i][j] = numpy.std(file_features_values[i][j]) #std
					features_variances_values[i][j].append(file_features_variances[i][j])
				else:
					file_features_means[i][j] = "Missing"
					file_features_variances[i][j] = "Missing"
	for i in range(1,13):
			for j in required_codes:
				features_means[i][j] = numpy.mean(features_means_values[i][j])
				features_variances[i][j] = numpy.mean(features_variances_values[i][j])
	count = 0
	for station_id in filelist: # calculate features
		if station_id[0] == '.': #system files
			continue
		count += 1
		if count % 1000 == 0:
			print count
		path = './stations/' + station_id
		f = open(path, "r")
		file_features_counts= [dict({'PRCP':0, 'SNOW':0, 'SNWD':0, 'TMAX':0, 'TMIN':0}) for i in range(15)]
		file_features_values = [dict({'PRCP':[], 'SNOW':[], 'SNWD':[], 'TMAX':[], 'TMIN':[]}) for i in range(15)]
		file_features_means = [dict({'PRCP':0, 'SNOW':0, 'SNWD':0, 'TMAX':0, 'TMIN':0}) for i in range(15)]
		file_features_variances = [dict({'PRCP':0, 'SNOW':0, 'SNWD':0, 'TMAX':0, 'TMIN':0}) for i in range(15)]
		required_codes = {'PRCP', 'SNOW', 'SNWD', 'TMAX', 'TMIN'}
		for line in f:		
			line = line.strip()
			year = int(line[0:4])
			month = int(line[4:6])
			day = int(line[6:8])
			code = line[9:13]
			num = int(line[14:])
			if code not in required_codes:
				continue
			file_features_values[month][code].append(num)
			file_features_counts[month][code] = file_features_counts[month][code]  + 1
		for i in range(1,13):
			for j in required_codes:
				if file_features_counts[i][j] > 0:
					file_features_means[i][j] = numpy.mean(file_features_values[i][j])
					file_features_variances[i][j] = numpy.var(file_features_values[i][j])
					#file_features_variances[i][j] = numpy.std(file_features_values[i][j]) #std

				else:
					file_features_means[i][j] = features_means[i][j]
					file_features_variances[i][j] = features_variances[i][j]
		f_out = open("./features/" + station_id+".csv", "a")
		for i in range(1,13):
			for j in required_codes:
				f_out.write(str(file_features_means[i][j])+","+str(file_features_variances[i][j])+",")
	print "done"