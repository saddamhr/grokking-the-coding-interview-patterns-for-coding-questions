class Solution:
    def average_of_contiguous_sub_arrays(self, nums, k):
        window_sum = window_start = 0
        res = []

        for window_end in range(len(nums)):
            window_sum += nums[window_end]
            if window_end >= k - 1:
                res.append(window_sum / k)
                window_sum -= nums[window_start]
                window_start += 1
        return res


print(Solution().average_of_contiguous_sub_arrays([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))


