from discrete_log import bsgs
from ClassicalShorsAlgo.faster_quantum_part import faster_quantum_part
from ClassicalShorsAlgo.deci_to_bin import deci_to_bin

def solve_discrete(generator, p, h):
    n_bits = len(deci_to_bin(p))

    measurement = faster_quantum_part(n_bits, p, generator)

    j = 1
    r = 0
    while True:
        r = j * (2**n_bits) * (1 / measurement)
    
        if (r - int(r)) == 0.0:
            break

        j += 1

    return_value = None

    for i in range(10):
        return_value = bsgs(generator, p, h, r)

        if return_value == None:
            r *= 2
            return_value = bsgs(generator, p, h, r)
        else:
            break

    return return_value


if __name__=="__main__":
    print(solve_discrete(5, 23, 11))
    print(solve_discrete(3, 11, 5))



