from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        window_start, max_len, max_count_ones = 0, 0, 0

        for window_end in range(len(nums)):
            if nums[window_end] == 1:
                max_count_ones += 1
            if window_end - window_start + 1 - max_count_ones > k:
                if nums[window_start] == 1:
                    max_count_ones -= 1
                window_start += 1
            max_len = max(max_len, window_end - window_start + 1)
        return max_len