class Solution:
    def smallest_sub_array_with_given_sum(self, nums, s):
        res = float('inf')
        window_start = 0
        window_sum  = 0
        
        for window_end in range(len(nums)):
            window_sum += nums[window_end]
            while window_sum >= s:
                res = min(res, window_end - window_start + 1)
                window_sum -= nums[window_start]
                window_start += 1
        return 0 if res == float('inf') else res


print(Solution().smallest_sub_array_with_given_sum([2, 1, 5, 2, 8], 7))
