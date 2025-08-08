class Solution(object):
    def returnToBoundaryCount(self, nums):
        count = 0
        tet = 0
        for i in nums:
            count-=i
            if count==0:
                tet+=1
        return tet
        """
        :type nums: List[int]
        :rtype: int
        """
        