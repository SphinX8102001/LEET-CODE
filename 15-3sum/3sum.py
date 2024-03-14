class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        length = len(nums)

        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates

            left, right = i + 1, length - 1

            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]

                if total_sum < 0:
                    left += 1
                elif total_sum > 0:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # Skip duplicates
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # Skip duplicates

                    left += 1
                    right -= 1

        return ans