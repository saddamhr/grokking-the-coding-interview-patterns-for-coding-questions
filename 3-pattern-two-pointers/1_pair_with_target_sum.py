from typing import List
class Solution:
    def targetSum(self, arr: List[str], target: int) -> List[int]:
        left, right = 0, len(arr) - 1
        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum == target:
                return [left, right]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]
    
# An Alternate approach
from typing import List
class Solution:
    def targetSum(self, arr: List[str], target: int) -> List[int]:
        nums = {}
        for i, num in enumerate(arr):
            if target - num in nums:
                return [nums[target - num], i]
            else:
                nums[arr[i]] = i
        return [-1, -1]