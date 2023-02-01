from math import radians, pow, sin, cos, sqrt, asin
# This function takes in the lat and long of an allotment garden, and the lat and long of an address, and returns the distance from the address to the allotment garden.
# The garden coordinates are retrieved from the environment file.

RADIUS = 6371
KILOMETER_TO_MILE = 1.609344


def lat_long_to_distance(garden_lat: float, garden_long: float, add_lat: float, add_long: float) -> float:
    latitude1, longitude1 = radians(garden_lat), radians(garden_long)
    latitude2, longitude2 = radians(add_lat), radians(add_long)
    c = haversine_formula(latitude1, longitude1, latitude2, longitude2)
    return c * RADIUS


def haversine_formula(latitude1, longitude1, latitude2, longitude2):
    dlat, dlon = latitude1 - latitude2, longitude1 - longitude2
    a = pow(sin(dlat / 2), 2) + cos(latitude1) * \
        cos(latitude2) * pow(sin(dlon / 2), 2)
    return 2 * asin(sqrt(a))

# print(lat_long_to_distance(1.336080, 103.722980, 1.293020, 103.805720)) #returns 10
