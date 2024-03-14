class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = x
        x = str(x)
        rev = x[-1:-len(x)-1:-1]
        if rev == x:
            return True
        else:
            return False