class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_start, max_len, char_last_index_map = 0, 0, {}
        for window_end in range(len(s)):
            if s[window_end] in char_last_index_map:
                window_start = max(window_start, char_last_index_map[s[window_end]] + 1)
            char_last_index_map[s[window_end]] = window_end
            max_len = max(max_len, window_end - window_start + 1)
        return max_len