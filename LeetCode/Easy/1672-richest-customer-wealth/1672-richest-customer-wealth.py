class Solution(object):
    def maximumWealth(self, accounts):
        res =[]
        for i in accounts:
            res.append(sum(i))
        return max(res)
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        