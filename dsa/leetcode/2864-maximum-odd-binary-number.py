# You are given a binary string s that contains at least one '1'.

# You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.

# Return a string representing the maximum odd binary number that can be created from the given combination.

# Note that the resulting string can have leading zeros.



def maximumOddBinaryNumber(self, str):
    s = [c for c in s]
    left = 0

    for i in range(len(s)):
        if s[i] == "1":
            s[i], s[left] = s[left], s[i]
            left += 1
    s[left - 1] , s[len(s)-1]= s[len(s)-1], s[left - 1]
    return "".join(s)
