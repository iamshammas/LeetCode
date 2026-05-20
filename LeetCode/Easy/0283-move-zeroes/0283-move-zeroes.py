class Solution(object):
    def moveZeroes(self, nums):
        count = nums.count(0)
        new_nums = [n for n in nums if n!=0]
        new_nums.extend([0]*count)
        nums[:]=new_nums
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        