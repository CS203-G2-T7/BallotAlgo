def ballot_selector(user_dist: dict, num_plots: int, dist_weight: dict) -> set(str):
    return ["winner1", "winner2", "... winner(num_plots)"]


ballot_selector.__doc__ = "From the user_dist dictionary, the num_plots, and dist_weight, calculate the list of winners."


# This function takes in a dictionary of users and their distance from an allotment garden user_dist = {"user1": 20.11, "user2": 3.52, "user3": 1.26}.
# The maximum number of winners is the num_plots = 1
# The dist_weight is the weight given to each user based on distance. dist_weight = {1: 10, 2: 5, 5: 3}
# This means (dist < 1; 10 points), (1 <= dist < 2; 5 points), (2 <= dist < 5; 3 points), (dist >= 5; 1 point). This also implies that the minimum num of points a user can get is 1 point.
# After randomly selecting num_plots winners, return the list of winners as a set.
