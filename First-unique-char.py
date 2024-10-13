"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:

Input: s = "loveleetcode"

Output: 2

Example 3:

Input: s = "aabb"

Output: -1


"""


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Create a dictionary to store the frequency (count) of each character
        char_freq = {}

        # Iterate through the string to count character frequencies (count)
        for char in s:
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1

        # Iterate through the string again to find the first non-repeating character
        for i in range(len(s)):
            if char_freq[s[i]] == 1:
                return i

        # If no non-repeating character is found, return -1
        return -1
