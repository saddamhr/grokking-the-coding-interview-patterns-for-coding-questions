class Solution:
    def max_sub_array_of_size_k(self, nums, k):
        window_sum = window_start = 0

        res = nums[0]

        for window_end in range(len(nums)):
            window_sum += nums[window_end]
            if window_end >= k -1:
                res = max(res, window_sum)
                window_sum -= nums[window_start]
                window_start += 1
        return res

print(Solution().max_sub_array_of_size_k([2, 1, 5, 1, 3, 2], 3))
