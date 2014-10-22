import find_geoloc_by_id as find


def get_cluster():
    cluster = []
    cluster.append( [
        ("Hoenggerberg", 47.402320, 8.495623, 1),
        ("Zurich Airport", 47.461311, 8.550554, 2)] )

    cluster.append( [
            ("Luzern", 47.060256, 8.297013, 1),
            ("Kapelbrueke", 47.045693, 8.355065, 2)] )

    return cluster

if __name__ == "__main__":
    lat, lon = find.find("AJ000037579")
    print lat, lon
