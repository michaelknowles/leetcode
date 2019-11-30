from typing import Dict

def longestPalindrome(s: str) -> str:
    palindrome = s[0] if len(s) >= 1 else ''

    if len(s) == 0:
        return ''

    for i, c in enumerate(s):
        # Stop if the found palindrome is longer than the rest of the string
        if len(palindrome) >= len(s[i:]):
            break

        current = c
        for j in range(i+1, len(s)):
            current += s[j]
            # Check if a palidrome was found
            # If last char equals first char, check the rest
            if s[j] == current[0]:
                if current == current[::-1] and len(current) > len(palindrome):
                    palindrome = current
    
    return palindrome
 
assert(longestPalindrome('aaaa') == 'aaaa')
assert(longestPalindrome('abcba') == 'abcba')
assert(longestPalindrome('a') == 'a')
assert(longestPalindrome('ac') == 'a' or 'c')
assert(longestPalindrome('babad') == 'bab' or 'aba')
assert(longestPalindrome('cbbd') == 'bb')
