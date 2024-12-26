class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_pivot(nums, low, high):
            low_2 = low
            high_2 = high
            if len(nums) == 1:
                return -1
            while low <= high:
                mid = (low + high)//2
                if nums[mid-1] > nums[mid]:
                    return mid    
                if mid+1<len(nums):
                        if nums[mid+1] < nums[mid]:
                            return mid+1         
                # if nums[mid-1] < nums[mid]:
                #     low = mid + 1
                # else:
                #     high = mid - 1
                if nums[mid]>nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1    
            return -1

        def BS(nums,low,high,target):
            while low<=high:
                mid = (low+high)//2
                if nums[low] == target:
                    return low
                if nums[high] == target:
                    return high    
                if nums[mid] == target:
                    return mid
                elif target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            return -1
        pivot = find_pivot(nums,0,len(nums)-1) 
        print(pivot)   
        if pivot != -1:
            v1 = BS(nums,0,pivot-1,target)
            v2 = BS(nums,pivot,len(nums)-1,target)
        else:
            v = BS(nums,0,len(nums)-1,target)
            return v
        if v1 != -1:
            v = v1
        else:
            v = v2
        return v


