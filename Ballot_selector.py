import math
# from dotenv import load_dotenv
import random
import ast
import os

# load_dotenv()
# DIST_WEIGHTS: dict = {0: 10, 1: 5, 5: 1}
# 0 <= a < 1 : 10
# 1 <= b < 5 : 5
# 5 <= c     : 1


def ballot_selector(user_dist: dict, num_plots: int, dist_weights: dict):
    user_pool: list = pool_generator(user_dist, dist_weights)
    winners = rand_selector(user_pool, num_plots)
    return winners


def pool_generator(user_dist: dict, dist_weights: dict) -> list:
    user_pool: list = list(user_dist.keys())

    for k, v in user_dist.items():  # iterate through users
        w = get_weight(v, dist_weights)
        for _ in range(w):
            user_pool.append(k)
    return user_pool


def get_weight(dist: int, dist_weights: dict) -> int:
    group: int = math.floor(dist)  # 3.14 -> 3
    while group not in dist_weights:
        group -= 1
    return dist_weights[group]


def rand_selector(pool: list, num: int) -> list:
    selected = []
    for _ in range(num):
        rand_idx = random.randint(0, len(pool) - 1)
        winner = pool[rand_idx]
        selected.append(winner)
        pool = [i for i in pool if i != winner]
    return selected


# user_dist = {'a': .4, 'b': 6, 'c': 4.1, 'd': 5.1, 'e': 0.9,
#              'f': 1.01, 'g': 3.2, 'h': 4.99, 'i': 5.0, 'j': 100}
# print(ballot_selector(user_dist, 5, DIST_WEIGHTS))
