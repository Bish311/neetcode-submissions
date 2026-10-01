class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Create two empty dictionaries to store character frequencies
        count_s = {}
        count_t = {}
        if len(s) != len(t):
            return False
        # Loop 1: Count frequency of each character in string s
        for char in s:
            if char in count_s:
                count_s[char] += 1
            else:
                count_s[char] = 1

        # Loop 2: Count frequency of each character in string t
        for char in t:
            if char in count_t:
                count_t[char] += 1
            else:
                count_t[char] = 1

        # Check if both dictionaries contain the exact same keys and counts
        if count_s == count_t:
            return True
        else:
            return False