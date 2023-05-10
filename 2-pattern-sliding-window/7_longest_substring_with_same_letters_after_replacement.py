class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_start, max_len, max_repeated_letter_count, hash_map = 0, 0, 0, {}

        for window_end in range(len(s)):
            hash_map[s[window_end]] = 1 + hash_map.get(s[window_end], 0)
            max_repeated_letter_count = max(max_repeated_letter_count, hash_map[s[window_end]])

            if window_end - window_start + 1 - max_repeated_letter_count > k:
                hash_map[s[window_start]] -= 1
                window_start += 1
            max_len = max(max_len, window_end - window_start + 1)
        return max_len