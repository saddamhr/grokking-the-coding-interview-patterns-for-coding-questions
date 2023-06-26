class Solution:
    def countTriplets(self, nums, n, target):
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
