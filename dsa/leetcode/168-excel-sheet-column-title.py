# Easy
# Topics
# Companies
# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...


# Example 1:

# Input: columnNumber = 1
# Output: "A"
# Example 2:

# Input: columnNumber = 28
# Output: "AB"
# Example 3:

# Input: columnNumber = 701
# Output: "ZY"


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # Time: O(logn) - Log base 26 of n
        res = ""
        while columnNumber > 0:
            remainder = (columnNumber - 1) % 26
            res += chr(ord('A') + remainder)
            columnNumber = (columnNumber - 1) // 26

        return res[::-1] # reverse output
