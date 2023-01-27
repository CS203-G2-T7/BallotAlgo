import random

def remove_duplicates(keyset, winner):
    resultant_list = []
    for key in keyset:
        if key != winner:
            resultant_list.append(key)
    return resultant_list

def ballot_selector(user_dist, num_plots, dictionary):
    
    keyset_fixed = list(user_dist.keys())
    keyset = list(user_dist.keys())
    dict_keys = list(dictionary.keys())

    for i in range(0, len(keyset_fixed)):
        idx = 0
        while(user_dist.get(keyset_fixed[i]) > dict_keys[idx]):
            if (idx < len(dict_keys) - 1):
                idx += 1
            else:
                break
        value = dictionary.get(dict_keys[idx])
        for j in range (value):
            keyset.append(keyset_fixed[i])
        
    output = set()

    for i in range(num_plots):
        size = len(keyset)
        idx = random.randint(0, size - 1)
        winner = keyset[idx]
        print(winner)
        output.add(winner)
        keyset = remove_duplicates(keyset, winner)
    
    return output

dictionary = {1:9, 2:4, 5:2}
user_dist = {'a':.4, 'b':6, 'c':4.1, 'd':5.1, 'e':0.9, 'f':1.01, 'g':3.2, 'h':4.99, 'i':5.0, 'j':100}
print(ballot_selector(user_dist, 5, dictionary))