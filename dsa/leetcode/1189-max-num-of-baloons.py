# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.
# Input: text = "loonbalxballpoon"
# Output: 2
# Example 3:

# Input: text = "leetcode"
# Output: 0
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text)
        balloon = Counter("balloon")

        res = len(text) #or float("int")
        for c in balloon:
            res = min(res, countText[c] // balloon[c])
        return res
