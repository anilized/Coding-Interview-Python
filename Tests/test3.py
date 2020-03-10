def binToDec(bin_value):
    bin_value = int(bin_value)
    # converting binary to decimal
    decimal_value = 0
    count = 0
    
    while(bin_value != 0):
        digit = bin_value % 10
        decimal_value = decimal_value + digit * pow(2, count)
        bin_value = bin_value//10
        count += 1

    # returning the result        
    return decimal_value

print(binToDec("000111010101000101001100100101000101001011010101010101100100100100100101001001001"))
print(int("000111010101000101001100100101000101001011010101010101100100100100100101001001001",2))