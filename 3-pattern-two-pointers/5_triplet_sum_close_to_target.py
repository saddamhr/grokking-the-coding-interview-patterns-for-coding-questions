from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
      n = len(nums)
      res = nums[0] + nums[1] + nums[2]
      nums.sort()
      for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]: continue
        l = i + 1
        r = n - 1
        while l < r:
          total = nums[i] + nums[l] + nums[r]
          if total == target: return total
          if abs(total - target) < abs(res - target):
            res = total
          if total < target:
            l += 1
          else: r -= 1
      return res
        