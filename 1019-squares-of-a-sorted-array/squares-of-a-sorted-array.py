class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squared_vals = []
        for i in nums:
            squared_vals.append(i**2)
        squared_vals.sort()
        return squared_vals