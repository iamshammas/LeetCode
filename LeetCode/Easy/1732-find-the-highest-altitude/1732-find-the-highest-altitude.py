class Solution(object):
    def largestAltitude(self, gain):
        c = [0]
        for i in gain:
            c.append(c[-1]+i)
        return max(c)
        """
        :type gain: List[int]
        :rtype: int
        """
        