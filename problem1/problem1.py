from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    # Loop through each number in list
    for idx, num in enumerate(nums):
        # Test adding rest of numbers in list to the given number
        # Start the second loop after the index of the given number
        # to avoid duplicate work
        for jdx, comp in enumerate(nums[idx+1:]):
            if target == comp + num:
                return [idx, jdx + idx + 1]

print(twoSum([2, 7, 11, 15], 9) == [0, 1])