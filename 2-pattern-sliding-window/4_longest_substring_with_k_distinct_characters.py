class Solution:
    def  longest_substring_with_k_distinct(self, str, k):
        max_length, window_start, hash_map = 0, 0, {}
        for window_end in range(len(str)):
            hash_map[str[window_end]] = 1 + hash_map.get(str[window_end], 0)

            while len(hash_map) > k:
                hash_map[str[window_start]] -= 1
                if hash_map[str[window_start]] == 0:
                    del hash_map[str[window_start]]
                window_start += 1
            max_length = max(max_length, window_end - window_start + 1)
        return max_length


print(Solution().longest_substring_with_k_distinct("aaaa", 2)) # -1
