from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window_start, max_len, hash_map = 0, 0, {}

        for window_end in range(len(fruits)):
            hash_map[fruits[window_end]] = 1 + hash_map.get(fruits[window_end], 0)
            while len(hash_map) > 2:
                hash_map[fruits[window_start]] -= 1
                if hash_map[fruits[window_start]] == 0:
                    del hash_map[fruits[window_start]]
                window_start += 1
            max_len = max(max_len , window_end - window_start + 1)
        return max_len
    
print(Solution().totalFruit([1, 2, 1]))