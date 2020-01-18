def isPalindrome(x: int) -> bool:
    val = str(x)
    if val == val[::-1]:
        return True   
    return False

assert(121 == True)
assert(-121 == False)
assert(10 == True)
