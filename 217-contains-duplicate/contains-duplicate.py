class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq_count = {}
        for i in nums:
            if i not in freq_count:
                freq_count[i] = 1
            else:
                freq_count[i] +=1
        for value in freq_count.values():
            if value>1:
                return True
        return False        