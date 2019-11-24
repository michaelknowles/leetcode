from typing import List

# This first solution is the naive, brute-force approach
# It has the least amount of space used (O(1)) but takes the longest (O(n^2))
def twoSum(nums: List[int], target: int) -> List[int]:
    # Loop through each number in list
    for idx, num in enumerate(nums):
        # Test adding rest of numbers in list to the given number
        # Start the second loop after the index of the given number
        # to avoid duplicate work
        for jdx, comp in enumerate(nums[idx+1:]):
            # The list may not be sorted so we cannot short-circuit
            if target == comp + num:
                return [idx, jdx + idx + 1]

print(twoSum([2, 7, 11, 15], 9) == [0, 1])
print(twoSum([2, 11, 15, 7], 9) == [0, 3])

# This solution should be the fastest possible (O(n)) since it only loops once
# It does require building a dictionary of up to n elements (O(n))
def twoSum2(nums: List[int], target: int) -> List[int]:
    # Create a dict of complements and indexes as we loop through
    complements = {}
    for idx, num in enumerate(nums):
        comp = target - num
        # If we've seen the complement, return the indexes
        if comp in complements:
            return [complements[comp], idx]
        else:
            complements[num] = idx

print(twoSum2([2, 7, 11, 15], 9) == [0, 1])
print(twoSum2([2, 11, 15, 7], 9) == [0, 3])