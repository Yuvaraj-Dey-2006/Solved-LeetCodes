class Solution(object):
    def twoSum(self, nums, target):
        seen = {}  # Stores value: index
        
        for i, num in enumerate(nums):

            # O(1) instantaneous lookup
            if (target - num) in seen:
                return [seen[(target - num)], i]
            
            # Record the index of the current number
            seen[num] = i