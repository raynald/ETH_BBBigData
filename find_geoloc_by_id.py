d = {}

def init():
    f = open("ghcnd-stations.txt", "r")
    for line in f:
        info = line.strip().split(" ")
        id1 = 1
        while len(info[id1])<2: id1 = id1 + 1
        id2 = id1 + 1
        while len(info[id2])<2: id2 = id2 + 1
        d[info[0]] = (info[id1], info[id2])

def find(name):
    return d[name][0], d[name][1]

