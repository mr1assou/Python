def hex_to_bin(h):
    result = ""
    for ch in h:
        if 'A' <= ch <= 'F':
            x = (ord(ch) - ord('A')) + 10
            result += dec_bin(str(x))
        else:
            result += dec_bin(ch)
    return result

def dec_bin(x):
    return bin(int(x, 16))[2:].zfill(4) + " "

hex_num = input("Please Enter the Hexadecimal Number: ")
binary_num = hex_to_bin(hex_num.upper())

print("Equivalent Binary Number is")
print(binary_num)
