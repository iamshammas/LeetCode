class Solution(object):
    def plusOne(self, digits):
        n = int(''.join(map(str,digits)))+1
        n = [int(i) for i in str(n)]
        return n
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        