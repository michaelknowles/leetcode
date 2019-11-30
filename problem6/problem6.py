# PAYPALISHIRING
# PAHNAPLSIIGYIR
# 14 chars
# 3 rows
# 0, 4, 8, 12 -- 4
# 1, 3, 5, 7, 9, 11, 13 -- 7
# 2, 5, 8 -- 3
# 
# PAYPALISHIRING
# PINALSIGYAHRPI
# 4 rows
# 0, 6, 12 -- 3
# 1, 5, 7, 11 -- 4
# 2, 4, 8, 10 -- 4
# 3, 9 -- 2
def convert(s: str, numRows: int) -> str:
    if numRows == 1: return s

    # using a dict here improved performance by around 40%
    # instead of a 2d array
    rows = {}
    i = 0 # row number
    down = False

    for c in s:
        if i not in rows:
            rows[i] = c
        else:
            rows[i] += c
        if i == 0 or i == (numRows-1):
            down = not down
        i += 1 if down else -1
    
    result = ''
    for i in range(0, numRows):
        if i in rows:
            result += rows[i]
    return result

assert(convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR')
assert(convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI')