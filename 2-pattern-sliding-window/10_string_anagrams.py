from typing import List
class Solution:
    def findAnagrams(self, s2: str, s1: str) -> List[int]:
        s1_counter = {}
        s2_counter = {}
        res = []

        for ch in s1:
            s1_counter[ch] = 1 + s1_counter.get(ch, 0)
        window_start = 0
        for window_end in range(len(s2)):
            s2_counter[s2[window_end]] = 1 + s2_counter.get(s2[window_end], 0)
            if window_end > len(s1) - 1:
                if s2_counter[s2[window_start]] == 1:
                    del s2_counter[s2[window_start]]
                else:
                    s2_counter[s2[window_start]] -= 1
                window_start += 1
            if s1_counter == s2_counter:
                res.append(window_start)
        return res