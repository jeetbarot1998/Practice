def int_to_Roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    i = 0
    while  num > 0:
        # print('outside',num // val[i])
        for _ in range(num // val[i]):
            # print(num // val[i])
            # print(i)
            # print(syb[i])
            # print(num)
            # print(val[i])
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num
number = 49
print(int_to_Roman(number))