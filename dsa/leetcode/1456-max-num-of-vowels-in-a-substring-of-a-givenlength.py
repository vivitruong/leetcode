# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.



# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
# Example 3:

# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l, res, total = 0, 0, 0
        vowels = "aeiou"

        for r in range(len(s)):
            if s[r] in vowels:
                total += 1
            if (r - l + 1) > k:
                if s[l] in vowels:
                    total -= 1
                l += 1
            res = max(res, total)
        return res

    #java

#     class Solution {
#     public int maxVowels(String s, int k) {
#         Set<Character> set = new HashSet<>();
#         Collections.addAll(set, 'a', 'e', 'i', 'o', 'u');

#         int l=0, cnt=0, res=0;

#         for(int r=0; r<s.length(); r++){
#             cnt += set.contains(s.charAt(r))?1:0;
#             if(r-l+1 > k){
#                 cnt -= set.contains(s.charAt(l))?1:0;
#                 l++;
#             }
#             res = Math.max(res, cnt);
#         }
#         return res;
#     }
# }


#javascript

# const maxVowels = (s, k) => {
#     // Time complexity O(n)
#     // Execution complexity O(1)
#     const vowels = "aeiou";
#     const n = s.length;
#     let start = 0;
#     let sum = 0;
#     let maxSum = 0;
#     for (let i = 0; i < n; i++) {

#         if (vowels.includes(s[i])) {
#             sum += 1;
#         }

#         if (i - start + 1 === k) {
#             maxSum = Math.max(sum, maxSum);
#             if (vowels.includes(s[start])) {
#                 sum--;
#             }
#             start++;
#         }
#     }

#     return maxSum;
# };

# Intuition
# break the problem in a easy way for better understanding

# Approach
# so, the problem says "Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k."

# to find the solution we need to determinate:

# the length of the string
# which letter is a vowel
# the length of our window
# the maximum number of vowels in the window
# we create a variable for store all the vowels for check later on if our current letters is a vowel

#     const vowels = "aeiou";
# take the length of the string "s" to iterate over

#     const n = s.length;
# create three variables for keep track of the window in the loop

# Start: initiated in 0, When the window is equal to our variable "k" keep track of the value at its index which would be the value outside our window.

# sum: initiated in 0, keep the number of vowel letters in any substring of s.
# maxSum: initiated in 0, keep the maximun number of vowels letters in any substring

#     let start = 0;
#     let sum = 0;
#     let maxSum = 0;
# iterate over the s length and check
# if the current index is a vowel, if that so add 1 to sum
# if the current i - start + 1 is equal to "k", check for the maximum value in the window and store it in maxSum
# if the start value is a vowels subtract one for keep the track of the window
# increments the start variable
# return the maximun value store in maxSum.
