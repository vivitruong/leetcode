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
