import random

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
            for j in range(9):              #add 10 tickets for people that stay within 1km
                keyset.append(keyset_fixed[i])
        elif user_dist.get(keyset_fixed[i]) <= 2:       
            for j in range(4):              #add 4 tickets for people that stay from 1km - 2km
                keyset.append(keyset_fixed[i])
        elif user_dist.get(keyset_fixed[i]) <= 5:       
            for j in range(2):              #add 3 tickets for people that stay from 2 - 5km
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

user_dist = {'a':.4, 'b':6, 'c':4.1, 'd':5.1, 'e':0.9, 'f':1.01, 'g':3.2, 'h':4.99, 'i':5.0, 'j':100}
print(ballot_selector(user_dist, 5))