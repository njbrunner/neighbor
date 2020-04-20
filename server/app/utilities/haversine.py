from math import radians, cos, sin, asin, sqrt

def haversine(longitude1: float, latitude1: float, longitude2: float, latitude2: float) -> float:
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    longitude1, latitude1, longitude2, latitude2 = map(radians, [longitude1, latitude1, longitude2, latitude2])

    # haversine formula 
    delta_longitude = longitude2 - longitude1 
    delta_latitude = latitude2 - latitude1 
    haversin = sin(delta_latitude/2)**2 + cos(latitude1) * cos(latitude2) * sin(delta_longitude/2)**2
    arc_haversin = 2 * asin(sqrt(haversin)) 
    radius = 3956 # Radius of earth in miles. Use 6371 for kilometers
    return arc_haversin * radius