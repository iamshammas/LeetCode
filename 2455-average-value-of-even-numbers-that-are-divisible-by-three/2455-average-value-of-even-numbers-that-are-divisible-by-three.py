class Solution(object):
    def averageValue(self, nums):
        tt = []
        for i in nums:
            if i%2 == 0:
                if i%3 == 0:
                    tt.append(i)
        if tt:
            result = sum(tt)//len(tt)
        else:
            result = 0

        return result
        """
        :type nums: List[int]
        :rtype: int
        """
        