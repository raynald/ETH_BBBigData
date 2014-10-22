def find(name):
    f = open("ghcnd-stations.txt", "r")
    for line in f:
        info = line.strip().split(" ")
        if info[0] == name:
            id1 = 1;
            while len(info[id1])<2: id1 = id1 + 1
            id2 = id1 + 1
            while len(info[id2])<2: id2 = id2 + 1
            return info[id1], info[id2]

