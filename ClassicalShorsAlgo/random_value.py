import random

def random_value(possible_nums_represented, probability_list):
    result = random.choices(possible_nums_represented, weights=probability_list, k=1)[0]
    
    # we don't want the zero measurements because
    # j * (2**n) * (1/r) = 0 will only result in
    # j = 0 and no values (well, technically, infinite values) for r
    if result != 0:
        return result
    
    return random_value(possible_nums_represented, probability_list)

