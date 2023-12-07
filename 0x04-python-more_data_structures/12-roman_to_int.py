#!/usr/bin/python3
def roman_to_int(roman_string):

    if roman_string is None or type(roman_string) != str:
        return(0)

    rom_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    to_num = [rom_num[elem] for elem in roman_string if elem in rom_num]

    resultado = 0

    for idx in range(len(to_num) - 1):
        if to_num[idx] >= to_num[idx + 1]:
            resultado += to_num[idx]
        else:
            resultado -= to_num[idx]
    return resultado + to_num[-1]
