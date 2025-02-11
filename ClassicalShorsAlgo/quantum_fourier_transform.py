import numpy as np
import scipy as sp

def quantum_fourier_matrix(n):
    columns_to_put_together = []

    for x_val in range(2**n):
        current_row = [[]]

        for y_val in range(2**n):
            exponent_power = -2 * np.pi * 1j * x_val * y_val * (1 / (2**n))
            exponent_value = np.exp(exponent_power)

            current_row[0].append(exponent_value)
        
        current_column = np.array(current_row).T

        columns_to_put_together.append(current_column)

    return np.column_stack(tuple(columns_to_put_together))
