def romanToInt(s: str) -> int:

    roman_map = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    n = len(s)
    integer_value = 0

    for i in range(n):

        current_char_value = roman_map[s[i]]

        if i + 1 < n and current_char_value < roman_map[s[i+1]]:
            integer_value -= current_char_value
        else:
            integer_value += current_char_value
    return integer_value


roman_input = input("Input roman numeral: ")

print("Integer equivalent:", romanToInt(roman_input))