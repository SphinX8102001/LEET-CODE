class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if -100.0 < x < 100.0 and -2**31 <= n <= 2**31-1:
            return x**n