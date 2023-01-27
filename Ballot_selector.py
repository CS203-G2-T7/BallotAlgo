import random

# This function takes in a dictionary of users and their distance from an allotment garden user_dist = {"user1": 20.11, "user2": 3.52, "user3": 1.26}.
# The maximum number of winners is the num_plots = 1
# The dist_weight is the weight given to each user based on distance. dist_weight = {1: 10, 2: 5, 5: 3}
# This means (dist < 1; 10 points), (1 <= dist < 2; 5 points), (2 <= dist < 5; 3 points), (dist >= 5; 1 point). This also implies that the minimum num of points a user can get is 1 point.
# After randomly selecting num_plots winners, return the list of winners as a set.


def remove_duplicates(keyset, winner):
    resultant_list = []
    for key in keyset:
        if key != winner:
            resultant_list.append(key)
    return resultant_list


def ballot_selector(user_dist, num_plots):

    keyset_fixed = list(user_dist.keys())
    keyset = list(user_dist.keys())

    for i in range(0, len(keyset_fixed)):
        if user_dist.get(keyset_fixed[i]) <= 1:
            for j in range(9):  # add 10 tickets for people that stay within 1km
                keyset.append(keyset_fixed[i])
        elif user_dist.get(keyset_fixed[i]) <= 2:
            for j in range(4):  # add 4 tickets for people that stay from 1km - 2km
                keyset.append(keyset_fixed[i])
        elif user_dist.get(keyset_fixed[i]) <= 5:
            for j in range(2):  # add 3 tickets for people that stay from 2 - 5km
                keyset.append(keyset_fixed[i])

    print(keyset)
    output = set()

    for i in range(num_plots):
        size = len(keyset)
        idx = random.randint(0, size - 1)
        winner = keyset[idx]
        print(winner)
        output.add(winner)
        keyset = remove_duplicates(keyset, winner)

    return output

#This is the old version. See Ballot_selector_test.py