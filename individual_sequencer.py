import math

def calc(a):
    arr = ["0", "2", "8", "9", "P", "Y", "L", "Q", "G", "R", "J", "C", "U", "V"]
    z = list(a)
    r = len(z)
    i = 0
    cummulative = 0
    while i < r:
        cummulative += arr.index(z[-1]) * math.pow(14, i)
        i += 1
        z = z[:-1]

    left = int(cummulative % 256)
    right = math.floor(cummulative / 256)
    print(dec2rdz(left) + ", " + dec2rdz(right))

def dec2rdz(num):
    _ = 0
    z = list(hex(num))[+2:]
    ret = ""
    while _ < 4:
        _ += 1
        if len(z) == 0:
            nr = "0"
        else:
            nr = z[-1]
            z = z[:-1]
        if len(z) == 0:
            nl = "0"
        else:
            nl = z[-1]
            z = z[:-1]
        nd = nl + nr
        ret = str(int(nd, 16)) + ", " + ret
    return ret[:-2]

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

choice = int(input('What do you want to calculate?\nType 0 for tag to number\nType 1 for number to tag\n'))

if choice == 0:
    tag = str(input("From what tag do you want to know the number? (Example: Type 2PP, NOT #2PP) "))
    tag = tag.upper()
    if '#' in tag:
        tag = tag.replace("#", "")
    calc(tag)
if choice == 1:
    numbers = str(input('Frow wich numbers do you want to know the tag? (Example: 0, 0, 0, 0, 0, 0, 0, 1) '))
    decalc(numbers)