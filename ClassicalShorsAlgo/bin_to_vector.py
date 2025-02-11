import scipy.linalg
from main import arr0, arr1

def bin_to_vector(input_string):
    first_digit_arr = arr0 if int(input_string[0]) == 0 else arr1
    second_digit_arr = arr0 if int(input_string[1]) == 0 else arr1

    output_array = scipy.linalg.kron(first_digit_arr, second_digit_arr)

    for digit in input_string[2:]:
        digit = int(digit)

        if digit == 0:
            output_array = scipy.linalg.kron(output_array, arr0)
        else:
            output_array = scipy.linalg.kron(output_array, arr1)

    return output_array


if __name__=="__main__":
    a = 3
    bin_a = bin(a)[2:]
    a_vector = bin_to_vector(bin_a)

    print(a_vector) # supposed to return an array with index 3 being one