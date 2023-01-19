import random
from Ballot_selector import ballot_selector

user_dist = {'a':.4, 'b':6, 'c':4.1, 'd':5.1, 'e':0.9, 'f':1.01, 'g':3.2, 'h':4.99, 'i':5.0, 'j':100}
print(ballot_selector(user_dist, 5))