class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height) - 1
        area = 0
        while i < j:
            temp = (j - i) * min(height[i], height[j])
            area = max(area, temp)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return area