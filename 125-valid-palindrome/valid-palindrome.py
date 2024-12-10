class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sum = ''
        s = s.lower()
        new_s=''
        for i in s:
            if 97<=ord(i)<=122 or 48<=ord(i)<=57:
                new_s+=i
        for i in range(len(s)-1,-1,-1):
            if 97<=ord(s[i])<=122 or 48<=ord(s[i])<=57:
                sum+=s[i]
        if sum == new_s:
            return True
        return False           
        