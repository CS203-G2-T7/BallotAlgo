# This function takes in the lat and long of an allotment garden, and the lat and long of an address, and returns the distance from the address to the allotment garden.
# The garden coordinates are retrieved from the environment file.

def lat_long_to_distance(garden_lat: float, garden_long: float, add_lat: float, add_long: float) -> float:
  return 0.0