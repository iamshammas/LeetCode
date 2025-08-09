class Solution(object):
    def maxDepth(self, s):
        c = 0
        deep = 0
        for i in s:
            if i == '(':
                c+=1
                if c > deep:
                    deep = c
            elif i == ')':
                c-=1
        return deep
        """
        :type s: str
        :rtype: int
        """
        