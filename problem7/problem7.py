def reverse(i:int) -> int:
    neg = False
    if i < 0:
        i = abs(i)
        neg = True

    nums = str(i)
    nums = nums[::-1]
    nums = int(nums)

    # Check for overflow
    if(nums > (2 ** 31 - 1)):
        return 0

    if neg:
        nums *= -1

    return nums

assert(reverse(1534236469) == 0)
assert(reverse(-123) == -321)
assert(reverse(123) == 321)
assert(reverse(120) == 21)