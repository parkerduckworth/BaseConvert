double_line = "=" * 50
single_line = "-" * 50


# Header
print()
print(double_line)
print("             Welcome to Base Convert.")
print(double_line)
print()
print("This program takes a decimal integer")
print("and converts it to any base")
print("up to hexadecimal.")
print()
print(single_line)


# Input collection
number = int(input("Enter number to convert: "))
print(single_line)
base = int(input("Enter base of conversion: "))
print(single_line)


# Main body of program
def main(number, base):
    sequence = []

    if base > 10:
        hex(number, base)
    else:
        for i in range(int(len(str(number)) / 0.301) + 1):  # k = log10(2) ≈ 0.301
            digit = get_remainder(number, base)
            sequence.append(digit)
            number = get_quotient(number, base)
    
        result = ''.join(reversed([str(x) for x in sequence]))
        print("Result: {}".format(result.lstrip('0')))
        print(single_line)
        prog_repeat()


# Handles integers with a base > 10, up to hexadecimal integers
def hex(number, base):
    sequence = []
    char_num_map = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}

    for i in range(int(len(str(number)) / 0.301) + 1):  # k = log10(2) ≈ 0.301
        digit = str(get_remainder(number, base))

        if int(digit) >= 10:
            digit = char_num_map[digit]

        sequence.append(digit)
        number = get_quotient(number, base)
    
    result = ''.join(reversed([str(x) for x in sequence]))
    print("Result: {}".format(result.lstrip('0')))
    print(single_line)
    prog_repeat()
    

# Allows for repeated sessions
def prog_repeat():
    recurse = input("Convert another integer? (Y/N): ")
    print(single_line)

    if recurse.upper() == 'Y':
        number = int(input("Enter number to convert: "))
        print(single_line)
        base = int(input("Enter base of conversion: "))
        print(single_line)

        if base > 10:
            hex(number, base)
        else:
            main(number, base)

    elif recurse.upper() == 'N':
        print("Goodbye!")
    else:
        print("Not a valid input.")
        prog_repeat()


# Calculates quotient to be used as next coefficient
def get_quotient(dividend, divisor):
    quotient = dividend // divisor
    return quotient


# Calculates remainder used as digit in result sequence
def get_remainder(dividend, divisor):
    remainder = dividend % divisor
    return remainder



# Executes program
main(number, base)