import numpy as np
import scipy as sp
import random
from ClassicalShorsAlgo.random_value import random_value

def faster_quantum_part(n_bits, number_to_factor, guess):
    initial_array = [[]]
    unique_numbers_in_initial_array = set()

    for i in range(2**n_bits):
        number_to_append = (guess**i) % number_to_factor
        unique_numbers_in_initial_array.add(number_to_append)

        initial_array[0].append(number_to_append)

    
    ###########################################

    unique_numbers_in_initial_array = list(unique_numbers_in_initial_array)
    measured_mod_value = random.choice(unique_numbers_in_initial_array)

    array_for_qft = initial_array.copy()
    non_zero_indeces = []

    for i in range(len(initial_array[0])):
        if initial_array[0][i] != measured_mod_value:
            array_for_qft[0][i] = 0
        else:
            array_for_qft[0][i] = 1
            non_zero_indeces.append(i)

    array_for_qft = np.array(array_for_qft).T

    end_of_qft_array = [[]]

    for y_val in range(2 ** n_bits):
        exponent_power = -2 * np.pi * 1j * non_zero_indeces[0] * y_val * (1 / (2**n_bits))
        exponent_value = np.exp(exponent_power)

        end_of_qft_array[0].append(exponent_value)

    end_of_qft_array = np.array(end_of_qft_array)
    
    for i in range(1, len(non_zero_indeces)):
        temp_array_to_add = [[]]

        for y_val in range(2 ** n_bits):
            exponent_power = -2 * np.pi * 1j * non_zero_indeces[i] * y_val * (1 / (2**n_bits))
            exponent_value = np.exp(exponent_power)

            temp_array_to_add[0].append(exponent_value)

        end_of_qft_array = end_of_qft_array + np.array(temp_array_to_add)

    end_of_qft_array = end_of_qft_array.T


    ###########################################

    for i in range(len(end_of_qft_array)):
        z = end_of_qft_array[i][0]

        real_z = z.real if abs(z.real) > 1e-10 else 0
        imag_z = z.imag if abs(z.imag) > 1e-10 else 0

        z = real_z + imag_z * 1j

        end_of_qft_array[i][0] = z


    # numpy outputs a numpy array with a numpy float.
    # So i access the first element to get the numpy 
    # float and convert it to a normal python float.
    norm = float(sp.linalg.norm(end_of_qft_array, axis=0)[0])
    possible_nums_represented = []
    probability_list = []
    for i in range(len(end_of_qft_array)):
        squared_mag = float(abs(end_of_qft_array[i][0]) ** 2) # converting numpy float to a normal float
        probability_list.append(squared_mag / (norm ** 2))

        possible_nums_represented.append(i)


    measurment = random_value(possible_nums_represented, probability_list)
    return measurment





