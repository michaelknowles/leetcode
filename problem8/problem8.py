MAX_INT = 2147483647
MIN_INT = -2147483648
ALL_NUMS = "0123456789"
SIGNS = "+-"

def myAtoi(str: str) -> int:
    str = str.lstrip()

    if len(str) == 0:
        return 0
        
    # Build the string of numbers
    num = str[0]
    if num not in SIGNS + ALL_NUMS:
        return 0
    for char in str[1:]:
        if char in ALL_NUMS:
            num += char
        else:
            break

    # Make sure the string has numbers in it
    if all([x not in num for x in ALL_NUMS]):
        return 0

    # Result must be within the 32 bit range
    result = int(num)
    if result < MIN_INT:
        return MIN_INT
    elif result > MAX_INT:
        return MAX_INT
    else:
        return result

assert(myAtoi("4193 with words") == 4193)
assert(myAtoi("+") == 0)
assert(myAtoi("  -42") == -42)
assert(myAtoi("words and 987") == 0)
assert(myAtoi("-91283472332") == -2147483648)
assert(myAtoi("+-2") == 0)
