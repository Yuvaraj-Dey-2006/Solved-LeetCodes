class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dup = {}

        for num in nums:
            dup[num] = dup.get(num, 0) + 1
            if dup[num] > len(nums) // 2:
                return num