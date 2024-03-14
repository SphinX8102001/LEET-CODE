class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        key_val = {}
        for i in nums:
            if str(i) not in key_val.keys():
                key_val[str(i)] = 0
        for i in nums:
            for k, c in key_val.items():
                if str(i) == k:
                    key_val[k] = c + 1
        print(key_val)
        vals = key_val.values()
        print(vals)
        max = float('-inf')
        # count = 0
        for i in vals:
            if i > max:
                max = i
                count = 1
            elif i == max:
                count+=1
        return max*count