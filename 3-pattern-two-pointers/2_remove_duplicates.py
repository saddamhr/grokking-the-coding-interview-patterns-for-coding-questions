from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        next_no_duplicate = 1
        i = 1
        while i < len(nums):
            if nums[next_no_duplicate - 1] != nums[i]:
                nums[next_no_duplicate] = nums[i]
                next_no_duplicate += 1
            i += 1
        return next_no_duplicate