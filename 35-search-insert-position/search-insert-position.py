class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if target not in nums:
            if n > 2:
                for i in range(1,n-1):
                    if nums[i-1]<=target<=nums[i+1]:
                        # print('yes')
                        if target<=nums[i]:
                            return i
                        return i+1
                if target>=nums[i+1]:
                    return i+2
                if target<=nums[0]:
                    return 0
            elif n==1:
                if target>=nums[0]:
                    return 1
                else:
                    return 0
            elif n==2:
                if target<=nums[0]:
                    return 0
                elif target>=nums[1]:
                    return 2
                elif nums[0]<target<nums[1]:
                    return 1

        else:
            for i in range(n):
                if nums[i] == target:
                    return i
