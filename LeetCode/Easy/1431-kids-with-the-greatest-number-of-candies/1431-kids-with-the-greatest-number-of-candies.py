class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        mx = max(candies)
        for i in range(len(candies)):
            j = candies[i]+extraCandies
            if j>=mx:
                candies[i]=True
            else:
                candies[i]=False
        return candies
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        