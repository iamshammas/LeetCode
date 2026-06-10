class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(c for c in s if c.isalnum()).lower()
        d = s[::-1].lower()
        return s==d
        """
        :type s: str
        :rtype: bool
        """
        