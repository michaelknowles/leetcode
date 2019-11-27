def lengthOfLongestSubstring(s: str) -> int:
    # Create a set to hold the substring chars
    chars = set()
    count = 0
    highest_count = 0
    # Create a new substring starting from each char
    for i in range(0, len(s)):
        subset = s[i:]
        # Loop through each char in the rest of the string
        for c in subset:
            if c in chars:
                # reset and build a new substring
                count = 0
                chars = set()
                break
            else:
                chars.add(c)
                count += 1
                if count > highest_count:
                    highest_count = count
    
    return highest_count

print(lengthOfLongestSubstring(" "), " == 1")
print(lengthOfLongestSubstring("jbpnbwwd"), " == 4")
print(lengthOfLongestSubstring("dvdf"), " == 3")
print(lengthOfLongestSubstring("abcabcbb"), " == 3")
print(lengthOfLongestSubstring("bbbbb"), " == 1")
print(lengthOfLongestSubstring("pwwkew"), " == 3")

