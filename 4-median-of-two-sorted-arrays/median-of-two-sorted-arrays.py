class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num3 = sorted(nums1 + nums2)
        total_data=len(num3)
        sum = 0
        if total_data%2==0:
            print('Even')
            index1 = total_data//2-1
            index2 = total_data//2
            sum = num3[index1]+num3[index2]
            median = sum/2
        else:
            print('Odd')
            index = (total_data+1)//2-1
            median=num3[index]
        print(median)
        return median