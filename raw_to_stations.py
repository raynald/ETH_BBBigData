import sys
#
#Sample input: US1FLSL0019,20090101,PRCP,0,,,N,
#

#def :

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        station_id = line[0:11]
        year = line[12:20]
        code = line[21:25]
        num = line[26:].split(',')[0]
        with open("./stations/" + station_id, "a") as myfile:
                myfile.write(year + " " + code+ " " + num + "\n")

