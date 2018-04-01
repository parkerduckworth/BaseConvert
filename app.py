# Parker Duckworth @parkerduckworth on 20180331


# Input collection
def initiate():
    try:
        number = int(input("Enter number to convert: "))
        print(single_line)
        base = int(input("Enter base of conversion: "))
        print(single_line)
        main(number, base)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        initiate()


# Main body of program
def main(number, base):
    sequence, negative = "", False
    hex_map = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    if number < 0:
        negative, number = True, number * -1

    if base < 2 or base > 16:
        print("Base must be an integer between 2 and 16")
        initiate()
    else:
        # k = log10(2) ≈ 0.301
        for i in range(int(len(str(number)) / 0.301) + 1):
            digit, number = get_remainder(number, base), get_quotient(number, base)
            
            if digit >= 10:
                digit = hex_map[digit]
            sequence += str(digit)
    
        result = sequence[::-1]
        print_result(result, negative)
  

# Allows for repeated sessions
def repeat_program():
    recurse = input("Convert another integer? (Y/N): ")
    print(single_line)

    if recurse.upper() == 'Y':
        initiate()
    elif recurse.upper() == 'N':
        print("ALL YOUR BASE ARE BELONG TO US.\nGoodbye!\n")
    else:
        print("Not a valid input.")
        repeat_program()


# Calculates quotient to be used as next coefficient
def get_quotient(dividend, divisor):
    return dividend // divisor


# Calculates remainder used as digit in result sequence
def get_remainder(dividend, divisor):
    return dividend % divisor


# Outputs result to the console
def print_result(result, negative):
    if negative:
        print("Result: -{}".format(result.lstrip('0')))
    else:
        print("Result: {}".format(result.lstrip('0')))
    print(single_line)
    repeat_program()


# Visual dividers
double_line, single_line = "=" * 50, "-" * 50


# Execute program
if __name__ == '__main__':
    print()
    print(double_line)
    print(" " * 13, "Welcome to BaseConvert")
    print(double_line)
    print("""
    This program takes a decimal integer
    and converts it to any base, between 
    binary and hexadecimal.""")
    print()
    print(single_line)
    initiate()
