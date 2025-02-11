from ClassicalShorsAlgo.faster_quantum_part import faster_quantum_part
from ClassicalShorsAlgo.greatest_common_divisor import greatest_common_divisor
import time
import decimal
from decimal import MAX_PREC

decimal.getcontext().prec = MAX_PREC

def faster_classical_shors_algo(n_bits, number_to_factor, guess):
    if guess ** 2 == number_to_factor:
        with open("database.txt", "a") as file:
            # Write the new data to the file
            file.write(str([guess, guess]) + "\n")

            file.close()
        
        return


    measurement = faster_quantum_part(n_bits, number_to_factor, guess)

    j = 1
    r = 0
    while True:
        r = j * (2**n_bits) * (1 / measurement)
        
        if (r - int(r)) == 0.0:
            break

        j += 1

    # print("guess:", guess)
    # print("r:", r)

    if int(r) % 2 == 1:
        # print("r is odd lmao")
        faster_classical_shors_algo(n_bits, number_to_factor, guess + 1)

    divisor1 = decimal.Decimal(guess) ** ( decimal.Decimal(r) / decimal.Decimal(2) ) + decimal.Decimal(1)
    divisor2 = decimal.Decimal(guess) ** ( decimal.Decimal(r) / decimal.Decimal(2) ) - decimal.Decimal(1)
    # print("divisors:", divisor1, divisor2)

    gcd1 = greatest_common_divisor(divisor1, decimal.Decimal(number_to_factor))
    gcd2 = greatest_common_divisor(divisor2, decimal.Decimal(number_to_factor))
    # print("gcds1:", gcd1, gcd2)
    return_list = [gcd1, gcd2]
    return_list_main = return_list.copy()
    # print("return_list5:", return_list)

    if (return_list[0] == 1) and (return_list[1] == 1):
        # print("hello1")
        faster_classical_shors_algo(n_bits, number_to_factor, guess + 1)
    elif return_list[0] == return_list[1]:
        # print("hello2")
        return_list[1] = number_to_factor / return_list[0]
        return_list_main = return_list.copy()
    elif return_list[0] == 1:
        # print("hello3")
        return_list[0] = number_to_factor / return_list[1]
        return_list_main = return_list.copy()
    elif return_list[1] == 1:
        # print("hello4")
        return_list[1] = number_to_factor / return_list[0]
        return_list_main = return_list.copy()

    # print("return_list5:", return_list)
    string = str([int(return_list_main[0]), int(return_list_main[1])])
    with open("database.txt", "a") as file:
        # Write the new data to the file
        file.write(string + "\n")

        file.close()
    # print(string)
    # print(divisor1, divisor2, number_to_factor)
    # print(divisor1, divisor2)
    return [int(return_list[0]), int(return_list[1])]