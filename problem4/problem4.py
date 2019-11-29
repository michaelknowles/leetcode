from typing import List
from math import floor 

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    # Only need to go through half of the numbers
    n1_count = len(nums1)
    n2_count = len(nums2)
    total_count = n1_count + n2_count
    half_count =  total_count / 2 if total_count % 2 == 0 else floor(total_count / 2)

    # Build a list containing numbers from both lists sorted into one
    xs: List[int] = []

    # Check if either list is empty
    if not nums1 and not nums2:
        return 0
    if not nums1:
        middle = floor(n2_count / 2)
        if n2_count % 2 == 1:
            return nums2[middle]
        else:
            return (nums2[middle] + nums2[middle-1]) / 2
    if not nums2:
        middle = floor(n1_count / 2)
        if n1_count % 2 == 1:
            return nums1[middle]
        else:
            return (nums1[middle] + nums1[middle-1]) / 2

    # Add items to list in ascending order
    n1 = nums1.pop(0)
    n2 = nums2.pop(0)
    while len(xs) <= half_count:
        if n1 is None and n2 is None:
            break
        if n1 is None:
            # n1 is None
            xs.append(n2)
            if nums2:
                n2 = nums2.pop(0)
            else:
                n2 = None
        elif n2 is None:
            # n2 is None
            xs.append(n1)
            if nums1:
                n1 = nums1.pop(0)
            else:
                n1 = None
        elif n1 > n2:
            xs.append(n2)
            if nums2:
                n2 = nums2.pop(0)
            else:
                n2 = None
        elif n2 > n1:
            xs.append(n1)
            if nums1:
                n1 = nums1.pop(0)
            else:
                n1 = None
        else:
            # n1 and n2 are the same
            # doesn't matter which one we insert
            # the other will be taken care of on next loop
            xs.append(n1)
            if nums1:
                n1 = nums1.pop(0)
            else:
                n1 = None
    
    median = xs[-1] if total_count % 2 == 1 else (xs[-1] + xs[-2]) / 2
    return float(median)

assert(findMedianSortedArrays([1,2],[1,2]) == 1.5)
assert(findMedianSortedArrays([],[1]) == 1.0)
assert(findMedianSortedArrays([0,0],[0,0]) == 0)
assert(findMedianSortedArrays([1,3],[2]) == 2.0)
assert(findMedianSortedArrays([1,2],[3,4]) == 2.5)