class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        a=0
        b=0
        res=0
        for i in nums:
            if i ==1:
                b+=1
            else:
                a = b if b>a else a
                b=0
            res = a if a>b else b
        return res
        """
        :type nums: List[int]
        :rtype: int
        """
        