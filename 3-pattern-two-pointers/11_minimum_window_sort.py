from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        u, l = 0, len(nums) - 1
        for i in range(len(nums)):
            if sorted_nums[i] != nums[i]:
                l = min(l, i)
                u = max(u, i)
        return 0 if l >= u else u - l + 1 
