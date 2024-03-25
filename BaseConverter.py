def bin_to_dec(number):
    number = str(number)
    reversed = number[::-1]
    result = 0
    for i in range(len(number)):
        result += int(reversed[i]) * 2**i
    print(result)

bin_to_dec(110111000101)

def hex_to_dec(number):
    number = str(number)
    reversed = number[::-1]
    result = 0
    for i in range(len(number)):
        if reversed[i].isalpha():
            result += (ord(reversed[i]) - 55)* 16**i
        else:
            result += int(reversed[i]) * 16**i
    print(result)

hex_to_dec('1AF2')


def dec_to_hex(number):
    result = ''
    while number > 16:
        quotient = number % 16
        if quotient > 9:
            result += chr(quotient + 55)
            number = number // 16
        else:
            result += str(quotient)
            number = number // 16
    else: result += str(number)
    print(result[::-1])

dec_to_hex(2555)

def dec_to_bin(number):
    result = ''
    while number >= 2:
        quotient = number % 2
        result += str(quotient)
        number = number // 2
    else: result += str(number)
    print(result[::-1])

dec_to_bin(2314)


def all_in_one(num):
    bin_num = bin(num)
    oct_num = oct(num)
    hex_num = hex(num)
    print(bin_num[2:])
    print(oct_num[2:])
    print(hex_num[2:].upper())

all_in_one(10)