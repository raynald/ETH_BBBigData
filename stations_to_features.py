import sys
import os

if __name__ == "__main__":
	filelist = os.listdir('./stations')
	features_sums = [dict({'PRCP':0, 'SNOW':0, 'SNWD':0, 'TMAX':0, 'TMIN':0}) for i in range(15)]
	features_counts= [dict({'PRCP':0, 'SNOW':0, 'SNWD':0, 'TMAX':0, 'TMIN':0}) for i in range(15)]
	i=0
	for station_id in filelist: #pre-processing for missing values
		if station_id[0] == '.': #system files
			continue
		i = i + 1
		if i % 1000 == 0:
			print i
		path = './stations/' + station_id
		f = open(path, "r")
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
			features_counts[month][code] = features_counts[month][code]  + 1
			features_sums[month][code] = features_sums[month][code] + num
	print "first phase done"
	for station_id in filelist:
		if station_id[0] == '.': #system files
			continue
		path = './stations/' + station_id
		f = open(path, "r")
		features = [dict() for i in range(15)]
		flag = True
		curmonth = 0
		month_counts = {'PRCP':0, 'SNOW':0, 'SNWD':0, 'TMAX':0, 'TMIN':0}
		month_sums = {'PRCP':0, 'SNOW':0, 'SNWD':0, 'TMAX':0, 'TMIN':0}
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
			if flag:
				curmonth = month
				flag = False
			if month == curmonth:
				month_counts[code] = month_counts[code] + 1
				month_sums[code] = month_sums[code] + num
			else:
				for k in month_counts.keys():
					if month_counts[k] == 0:
						if features_counts[curmonth][k] > 0:
							features[curmonth][k] = features_sums[curmonth][k]/features_counts[curmonth][k]
						else:
							features[curmonth][k] = 0
					else:
						features[curmonth][k] = month_sums[k] / month_counts[k]
				curmonth = month
				month_counts = {'PRCP':0, 'SNOW':0, 'SNWD':0, 'TMAX':0, 'TMIN':0}
				month_sums = {'PRCP':0, 'SNOW':0, 'SNWD':0, 'TMAX':0, 'TMIN':0}
				month_counts[code] = month_counts[code] + 1
				month_sums[code] = month_sums[code] + num
		for k in month_counts.keys():
			if month_counts[k] == 0:
				if features_counts[curmonth][k] > 0:
					features[curmonth][k] = features_sums[curmonth][k]/features_counts[curmonth][k]
				else:
					features[curmonth][k] = 0
			else:
				features[curmonth][k] = month_sums[k] / month_counts[k]
		f_out=open("./features/" + station_id+".csv", "a")					
		for i in range(1,curmonth+1):
			for j in features[i].keys():
				f_out.write(str(features[i][j])+",")