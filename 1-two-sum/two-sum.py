class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index =[]
        i = 0
        while i<len(nums):
            k = i+1
            while k < len(nums):
                sum = nums[i]+nums[k]
                if sum == target:
                    index.append(i)
                    index.append(k)
                k+=1
            i+=1        
        return index            