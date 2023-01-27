# This function takes in the lat and long of an allotment garden, and the lat and long of an address, and returns the distance from the address to the allotment garden.
# The garden coordinates are retrieved from the environment file.
from math import radians, pow, sin, cos, sqrt, asin

def lat_long_to_distance(garden_lat: float, garden_long: float, add_lat: float, add_long: float) -> float:
    #radius of earth in KM
    RADIUS = 6371;

    #converts miles to KM
    KILOMETER = 1.609344;

    latitude1 = radians(garden_lat)
    longitude1 = radians(garden_long)
    latitude2 = radians(add_lat)
    longitude2 = radians(add_long)

    c = haversine_formula(latitude1, longitude1, latitude2, longitude2)

    return c * RADIUS * KILOMETER

def haversine_formula(latitude1, longitude1, latitude2, longitude2):
    dlat = latitude1 - latitude2
    dlon = longitude1 - longitude2
    print(dlon)
    print(dlat)

    a = pow(sin(dlat / 2), 2) + cos(latitude1) * cos(latitude2) * pow(sin(dlon / 2), 2)
    print(a)
    return 2 * asin(sqrt(a))

print(lat_long_to_distance(1.336080, 103.722980, 1.293020, 103.805720))