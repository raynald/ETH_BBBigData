#!/usr/bin/python
import sys
import numpy as np

codeSet = {'PRCP':0, 'SNOW':1, 'SNWD':2, 'TMAX':3, 'TMIN':4}
feature = []
feature += [np.array([])]
feature += [np.array([])]
feature += [np.array([])]
feature += [np.array([])]
feature += [np.array([])]

feature_mean = np.array([21.946847, 3.553948, 55.310004, 170.481257, 42.115845])
feature_var =  np.array([6899.758664, 514.271678, 49495.052299, 15268.886236, 12898.279059])
normalize_mean = np.array([[231.01169, 427.867596, 831.226235, 355.821118, -494.689006],[246.341824, 253.539213, 869.217852, 640.420745, -323.544331],[226.501026, 332.702289, 610.83667, 1191.605142, 113.883425],[246.597529, 231.773927, 253.306121, 1873.669713, 693.415982],[311.311214, 76.560816, 69.259884, 2498.595248, 1271.70497],[420.040241, 26.932759, 13.387138, 3003.313626, 1736.392004],[395.476327, 2.260238, 3.108542, 3286.516097, 1990.683921],[367.366978, 1.455422, 2.541279, 3204.222213, 1912.834525],[306.560313, 19.001422, 2.619931, 2711.72149, 1489.790296],[281.865766, 212.12079, 19.297086, 1968.894539, 891.618353],[258.875551, 380.314261, 175.044852, 1151.644207, 278.899001],[215.737482, 380.462773, 494.086928, 566.46753, -232.547664]])
normalize_var =  np.array([[41081.926176, 156494.828972, 409055.86414, 82289.759804, 132308.893045],[46430.182503, 52955.506388, 428029.578078, 267910.27574, 55007.844296],[39138.765667, 95300.272556, 247163.799486, 888740.16025, 28566.392396],[46305.286358, 47332.473813, 88811.013367, 2213787.94579, 366791.332917],[73931.505652, 5309.40055, 26582.774052, 3963260.35275, 1144821.14835],[132390.404997, 735.63005, 6251.40993, 5723897.25297, 2056608.48677],[114730.966949, 88.295211, 1705.996902, 6834786.36021, 2664888.05209],[99685.111971, 44.227878, 375.2258, 6501487.7553, 2474208.07408],[69774.648484, 418.696186, 512.876991, 4610977.92144, 1520499.14013],[60782.095449, 40417.766369, 2442.949695, 2394895.81094, 582189.78656],[51737.987361, 128146.966884, 45415.777, 806406.400239, 82556.22427],[35381.455559, 124417.518224, 146713.822337, 206752.831356, 28262.764463]])

def normalize(value,month,code):
    return (value - normalize_mean[month][code]) / normalize_var[month][code] * 1000

old_key = ""
old_year = ""
old_month = ""
outstring = ""
if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        key, year, month, code, num = line.split('\t')
        if code in codeSet:
            if old_key == "":
                old_key = key
                old_year = year
                old_month = month
            if key == old_key and year == old_year:
                if month == old_month:
                    feature[codeSet[code]] = np.append(feature[codeSet[code]], [normalize(int(num),int(month)-1,codeSet[code])])
                else:
                    for i in range(5):
                        if feature[i].size > 0:
                            outstring += "%f,%f," % (feature[i].mean(), feature[i].var())  
                        else:
                            outstring += "%f,%f," % (0, 0)   
                        feature[i] = np.array([])
                    old_month = month
                    feature[codeSet[code]] = np.append(feature[codeSet[code]], [normalize(int(num),int(month)-1,codeSet[code])])
            else:
                print "%s\t%s\t%s" % (old_key, old_year, outstring)
                old_key = key
                old_year = year
                outstring = ""
    for i in range(5):
        if feature[i].size > 0:
            outstring += "%f,%f," % (feature[i].mean(), feature[i].var())  
        else:
            outstring += "%f,%f," % (feature_mean[i], feature_var[i])    

    print "%s\t%s\t%s" % (old_key, old_year, outstring)
 