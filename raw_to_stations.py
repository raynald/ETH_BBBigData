import sys
"""
Sample input: US1FLSL0019,20090101,PRCP,0,,,N,
Sample output: SP000008027 20090101    TMAX    146
"""

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        station_id = line[0:11]
        date = line[12:20]
        code = line[21:25]
        num = line[26:].split(',')[0]
        print "%s\t%s\t%s\t%s" % (station_id, date, code, num)

