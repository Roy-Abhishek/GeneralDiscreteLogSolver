def greatest_common_divisor(input1, input2):
    used_input1 = max(input1, input2)
    used_input2 = min(input1, input2)

    remainder = used_input1 % used_input2

    if remainder == 0:
        return used_input2
    else:
        return greatest_common_divisor(used_input2, remainder)





if __name__=="__main__":
    print(greatest_common_divisor(1785, 546)) # prints 21


