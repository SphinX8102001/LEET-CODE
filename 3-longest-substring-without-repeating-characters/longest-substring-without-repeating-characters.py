class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = []
        sum = ""
        n = len(s)
        i = 0
        count = 0
        while i < n:
            # print(i,count)
            if s[i] not in sum:
                sum+=s[i]
                count += 1
            else:
                arr.append(sum)
                sum=""
                i = i-count
                count = 0
            i+=1
        arr.append(sum)
        # print(arr)
        # a = max(arr)
        largest = float('-inf')
        for i in arr:
            if len(i)>largest:
                largest = len(i)
                # temp = i
        return largest