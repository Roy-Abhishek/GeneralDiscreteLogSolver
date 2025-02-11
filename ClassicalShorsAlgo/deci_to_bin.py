def deci_to_bin_with_bits(a, n):
    binary_a = bin(a)[2:]
    current_n = len(binary_a)
    appended_zeros = n - current_n
    appending_string = "0" * appended_zeros

    return appending_string + binary_a

def deci_to_bin(a):
    return bin(a)[2:]


if __name__=="__main__":
    a = 10
    b = bin(a) # b is of type string --- "0b1010"
    c = deci_to_bin(a)

    print(c)
    print(deci_to_bin_with_bits(a, 8))

    print(int(c))
    print(int(c[1]))
    print(len(c))
