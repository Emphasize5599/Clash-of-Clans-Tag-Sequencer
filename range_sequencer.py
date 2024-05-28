import math
import contextlib
import io

def base10_to_base256(number):
    base256_values = [0] * 8  # Initialize an array of 8 zeros
    index = 7  # Start from the rightmost (least significant) byte
    while number > 0 and index >= 0:
        remainder = number % 256
        base256_values[index] = remainder
        number = number // 256
        index -= 1
    return ', '.join(map(str, base256_values))  # Convert the list to a comma-separated string

def generate_256_values(start, end):
    if start > end:
        return {}

    values_256 = {}
    for num in range(start, end + 1):
        values_256[num] = base10_to_base256(num)

    return values_256

start_range = int(input("Enter the start of the range (base 10): "))
end_range = int(input("Enter the end of the range (base 10): "))

values_256 = generate_256_values(start_range, end_range)

# The dictionary values_256 is now available for later use

DIGITS = '0123456789abcdef'
def convert_to_base(decimal_number, base):
    remainder_stack = []

    while decimal_number > 0:
        remainder = decimal_number % base
        remainder_stack.append(remainder)
        decimal_number = decimal_number // base

    new_digits = []
    while remainder_stack:
        new_digits.append(DIGITS[remainder_stack.pop()])

    return ''.join(new_digits)

def decalc(a):
    tz = a.split(" ")
    tz = "".join(tz)
    tz = tz.split(",")
    if len(tz) != 8:
        return
    i = 0
    while i < len(tz):
        tz[i] = int(tz[i])
        i += 1
    low = 0
    high = 0
    i = 0
    while i < 4:
        low += tz[i]
        low *= 0x100
        i += 1
    low /= 0x100
    i = 4
    while i < 8:
        high += tz[i]
        high *= 0x100
        i += 1
    high /= 0x100
    total = int(low + high * 0x100)
    out = convert_to_base(total, 14)
    out = list(out)
    arr = ["0", "2", "8", "9", "P", "Y", "L", "Q", "G", "R", "J", "C", "U", "V"]
    i = 0
    while i < len(out):
        out[i] = arr[int(out[i], 16)]
        i += 1
    print("".join(out))

# Function to run decalc for each value in the dictionary and capture the output
def run_decalc_and_capture_output(values_dict, output_file):
    # Create a StringIO object to capture the print output
    output_capture = io.StringIO()
    
    # Redirect stdout to the StringIO object
    with contextlib.redirect_stdout(output_capture):
        for value in values_dict.values():
            decalc(value)
    
    # Write the captured output to the specified file
    with open(output_file, 'w') as file:
        file.write(output_capture.getvalue())

# Run the function
run_decalc_and_capture_output(values_256, 'tags.txt')