from main import *
from ClassicalShorsAlgo.deci_to_bin import *
from ClassicalShorsAlgo.bin_to_vector import *
import numpy as np
import scipy as sp
from ClassicalShorsAlgo.quantum_fourier_transform import *
import random
from ClassicalShorsAlgo.random_value import *
from ClassicalShorsAlgo.greatest_common_divisor import *
import decimal



decimal.getcontext().prec = 1000

n_bits = 4
a = 5
b = 3


bin_a = deci_to_bin_with_bits(a, n_bits)
vector_a = bin_to_vector(bin_a)
# print(bin_a)
# print(vector_a)
# print()

bin_b = deci_to_bin_with_bits(b, n_bits)
vector_b = bin_to_vector(bin_b)
# print(bin_b)
# print(vector_b)
# print()

vector_c = vector_a + vector_b
# print(vector_c)


########################################
########################################
########################################


n_bits = 3

# print(2**n_bits)


if __name__=="__main__":
    pass


########################################
########################################
########################################


array1 = np.array([[1], [2], [3], [4]])
array2 = np.array([[5], [6], [7], [8]])
array3 = np.array([[1], [2], [3], [4]])
array4 = np.array([[5], [6], [7], [8]])

matrix1 = np.column_stack((array1, array2, array3, array4))
matrix2 = np.column_stack((array1, array2, array3, array4))

# print(matrix1)

matrix3 = sp.linalg.kron(matrix1, matrix2)

# print(matrix3)


########################################
########################################
########################################


exp = np.exp(1j * np.pi)
# print(exp)


result_list = [[]]

x_val = 0
for y_val in range(4):
    exponent_power = 2 * np.pi * 1j * x_val * y_val * (1 / 4)
    exponent_value = np.exp(exponent_power)

    result_list[0].append(exponent_value)

array = np.array(result_list)
array_transposed = array.T

# print(array_transposed)

array5 = np.array([[1], [2], [3], [4]])
array5_transposed = array5.T
# print(array5_transposed)
prod = array5_transposed @ array5
# print(prod[0][0])



########################################
########################################
########################################


# THE QUANTUM FOURIER MATRIX

zeroeth_column = [[]]
x_val0 = 0
for y_val in range(4):
    exponent_power = 2 * np.pi * 1j * x_val0 * y_val * (1 / 4)
    exponent_value = np.exp(exponent_power)

    zeroeth_column[0].append(exponent_value)
zeroeth_column = np.array(zeroeth_column).T

first_column = [[]]
x_val1 = 1
for y_val in range(4):
    exponent_power = 2 * np.pi * 1j * x_val1 * y_val * (1 / 4)
    exponent_value = np.exp(exponent_power)

    first_column[0].append(exponent_value)
first_column = np.array(first_column).T

second_column = [[]]
x_val2 = 2
for y_val in range(4):
    exponent_power = 2 * np.pi * 1j * x_val2 * y_val * (1 / 4)
    exponent_value = np.exp(exponent_power)

    second_column[0].append(exponent_value)
second_column = np.array(second_column).T

third_column = [[]]
x_val3 = 3
for y_val in range(4):
    exponent_power = 2 * np.pi * 1j * x_val3 * y_val * (1 / 4)
    exponent_value = np.exp(exponent_power)

    third_column[0].append(exponent_value)
third_column = np.array(third_column).T


result_array = np.column_stack((zeroeth_column, first_column, second_column, third_column))

# print(result_array)

identity = np.identity(2)

# print(result_array)
# print(quantum_fourier_matrix(2))
# print(result_array == quantum_fourier_matrix(2))



########################################
########################################
########################################







n = 6

N = 33
g = 6

initial_array = [[]]
unique_numbers_in_initial_array = set()

for i in range(2**n):
    number_to_append = (g**i) % N
    unique_numbers_in_initial_array.add(number_to_append)

    initial_array[0].append(number_to_append)

# initial_array = np.array(initial_array).T

# print(initial_array)

# notice it takes some to execute this program

###########################################


unique_numbers_in_initial_array = list(unique_numbers_in_initial_array)
# print(unique_numbers_in_initial_array)
measured_mod_value = random.choice(unique_numbers_in_initial_array)
# print(measured_mod_value)

array_for_qft = initial_array.copy()

for i in range(len(initial_array[0])):
    if initial_array[0][i] != measured_mod_value:
        array_for_qft[0][i] = 0
    else:
        array_for_qft[0][i] = 1

array_for_qft = np.array(array_for_qft).T


qft_matrix = quantum_fourier_matrix(n)


end_of_qft_array = qft_matrix @ array_for_qft

print(end_of_qft_array)


# norm = sp.linalg.norm(end_of_qft_array, axis=0) 
# print(sp.linalg.norm(end_of_qft_array, axis=0))


###########################################


for i in range(len(end_of_qft_array)):
    z = end_of_qft_array[i][0]

    real_z = z.real if abs(z.real) > 1e-10 else 0
    imag_z = z.imag if abs(z.imag) > 1e-10 else 0

    z = real_z + imag_z * 1j

    end_of_qft_array[i][0] = z

print(end_of_qft_array)


norm = float(sp.linalg.norm(end_of_qft_array, axis=0)[0]) # numpy outputs a numpy array with a numpy float. So i access the first element to get the numpy float and convert it to a normal python float.
possible_nums_represented = []
probability_list = []
for i in range(len(end_of_qft_array)):
    squared_mag = float(abs(end_of_qft_array[i][0]) ** 2) # converting numpy float to a normal float
    probability_list.append(squared_mag / (norm ** 2))

    possible_nums_represented.append(i)

result = random_value(possible_nums_represented, probability_list)

print(result)
print()
print()
print()



###########################################


j = 1
r = 0
while True:
    r = j * (2**n) * (1 / result)
    
    if (r - int(r)) == 0.0:
        print("this is r:", r)
        break

    j += 1

# if r is not even, we gotta do the whole process again so probably make the above into one function

divisor1 = g ** (r/2) + 1
divisor2 = g ** (r/2) - 1


gcd1 = greatest_common_divisor(divisor1, N)
gcd2 = greatest_common_divisor(divisor2, N)

print(gcd1, gcd2)







########################################
########################################
########################################
# second try







n = 8

N = 209
g = 14

initial_array = [[]]
unique_numbers_in_initial_array = set()

for i in range(2**n):
    number_to_append = (g**i) % N
    unique_numbers_in_initial_array.add(number_to_append)

    initial_array[0].append(number_to_append)

# initial_array = np.array(initial_array).T

# print(initial_array)

# notice it takes some to execute this program

###########################################


unique_numbers_in_initial_array = list(unique_numbers_in_initial_array)
# print(unique_numbers_in_initial_array)
measured_mod_value = random.choice(unique_numbers_in_initial_array)
# print(measured_mod_value)

array_for_qft = initial_array.copy()

for i in range(len(initial_array[0])):
    if initial_array[0][i] != measured_mod_value:
        array_for_qft[0][i] = 0
    else:
        array_for_qft[0][i] = 1

array_for_qft = np.array(array_for_qft).T


qft_matrix = quantum_fourier_matrix(n)


end_of_qft_array = qft_matrix @ array_for_qft

print(end_of_qft_array)


# norm = sp.linalg.norm(end_of_qft_array, axis=0) 
# print(sp.linalg.norm(end_of_qft_array, axis=0))


###########################################


for i in range(len(end_of_qft_array)):
    z = end_of_qft_array[i][0]

    real_z = z.real if abs(z.real) > 1e-10 else 0
    imag_z = z.imag if abs(z.imag) > 1e-10 else 0

    z = real_z + imag_z * 1j

    end_of_qft_array[i][0] = z

print(end_of_qft_array)


norm = float(sp.linalg.norm(end_of_qft_array, axis=0)[0]) # numpy outputs a numpy array with a numpy float. So i access the first element to get the numpy float and convert it to a normal python float.
possible_nums_represented = []
probability_list = []
for i in range(len(end_of_qft_array)):
    squared_mag = float(abs(end_of_qft_array[i][0]) ** 2) # converting numpy float to a normal float
    probability_list.append(squared_mag / (norm ** 2))

    possible_nums_represented.append(i)

result = random_value(possible_nums_represented, probability_list)

print(result)
print()
print()
print()



###########################################


j = 1
r = 0
while True:
    r = j * (2**n) * (1 / result)
    
    if (r - int(r)) == 0.0:
        print("this is r:", r)
        break

    j += 1

# if r is not even, we gotta do the whole process again so probably make the above into one function

divisor1 = decimal.Decimal(g) ** ( decimal.Decimal(r) / decimal.Decimal(2) ) + decimal.Decimal(1)
divisor2 = decimal.Decimal(g) ** ( decimal.Decimal(r) / decimal.Decimal(2) ) - decimal.Decimal(1)


gcd1 = greatest_common_divisor(divisor1, N)
gcd2 = greatest_common_divisor(divisor2, N)

print(gcd1, gcd2)























########################################
########################################
########################################

# print()
# print()
# print()
# print()

# decimal.getcontext().prec = 100

# x = decimal.Decimal(3)
# y = decimal.Decimal(7)

# print(x + y)
# print(x + 4 == y)

# print(int(x))
