from typing import List

class Solution:
    def tripletsWithSmallerSum(self, nums: List[int], target: int) -> int:
      n = len(nums)
      res = 0
      nums.sort()
      for i in range(n - 2):
        l = i + 1
        r = n - 1
        while l < r:
          total = nums[i] + nums[l] + nums[r]
          if total < target:
            res += r - l
            l += 1
          else: r -= 1
      return res
        
print(Solution().tripletsWithSmallerSum([-2, 0, 1, 3], 2))