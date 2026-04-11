class Solution(object):
    def runningSum(self, nums):
        res = []
        t = 0
        for i in range(len(nums)):
            t += nums[i]
            res.append(t)
        return res
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        