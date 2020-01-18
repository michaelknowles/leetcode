def isPalindrome(x: int) -> bool:
    val = str(x)
    if val == val[::-1]:
        return True   
    return False

assert(isPalindrome(121) == True)
assert(isPalindrome(-121) == False)
assert(isPalindrome(10) == True)
