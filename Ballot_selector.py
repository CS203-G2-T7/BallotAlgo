import random

# key is the distance, value is the number of additional tickets to be added
default_dist_weights = {1: 5, 2: 3, 5: 1}


def ballot_selector(user_dist: dict, num_plots: int, dist_weights: dict = default_dist_weights):
    keyset_fixed = list(user_dist.keys())
    keyset = list(user_dist.keys())
    dict_keys = list(dist_weights.keys())

    for i in range(0, len(keyset_fixed)):
        idx = 0
        while (user_dist.get(keyset_fixed[i]) > dict_keys[idx]):
            if (idx < len(dict_keys) - 1):
                idx += 1
            else:
                break
        value = dist_weights.get(dict_keys[idx])
        for j in range(value):
            keyset.append(keyset_fixed[i])

    output = set()
    for i in range(num_plots):
        size = len(keyset)
        idx = random.randint(0, size - 1)
        winner = keyset[idx]
        # print(winner)
        output.add(winner)
        keyset = [k for k in keyset if k != winner]
    return output


# user_dist = {'a': .4, 'b': 6, 'c': 4.1, 'd': 5.1, 'e': 0.9,
#              'f': 1.01, 'g': 3.2, 'h': 4.99, 'i': 5.0, 'j': 100}
# print(ballot_selector(user_dist, 5, dist_weights))
