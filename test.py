import find_geoloc_by_id as find

def get_cluster(yearid):
    find.init()
    cluster = []
    for i in range(300): cluster.append([])
    a = []
    for i in range(300): a.append(0)
    with open("result/by_year_300n3/"+str(yearid)+'.label', "r") as f:
        for line in f:
            ausweis = line.split(" ")
            id_ = ausweis[0]
            num = int(ausweis[1])
            lat, lon = find.find(id_)
            a[num] = a[num] + 1
            cluster[num].append((id_, lat, lon, a[num]))
    """
    cluster = []
    cluster.append( [
         ("Hoenggerberg", 47.402320, 8.495623, 1),
         ("Zurich Airport", 47.461311, 8.550554, 2)] )
    cluster.append( [
         ("Luzern", 47.060256, 8.297013, 1),
         ("Kapelbrueke", 47.045693, 8.355065, 2)] )
    """
    return cluster

if __name__ == "__main__":
    pass
