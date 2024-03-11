class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        arr = []
        if nums1>=nums2:
            a = nums1
            b = nums2
        else:
            a = nums2
            b = nums1
        for i in a:
            if i in b and i not in arr:
                arr.append(i)        
        return arr        